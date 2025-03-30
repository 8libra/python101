#! /usr/bin/env python
# Usage: python apple_bssid_locator.py <-b BSSID | -l BSSID_list> [-o output_file]
# Credit: Original code by Darko Sancanin at https://github.com/darkosancanin/apple_bssid_locator
import sys
import csv
from argparse import ArgumentParser
import re
try:
    import requests
except ModuleNotFoundError:
    print("The `requests` module is required. Install it with `python -m pip install requests`", file = sys.stderr)
    sys.exit(1)
try:
    import AppleWLoc_pb2
except ModuleNotFoundError:
    print("The `protobuf` module is required. Install it with `python -m pip install protobuf`", file = sys.stderr)
    sys.exit(2)


api_endpoint = "https://gs-loc.apple.com/clls/wloc"
# Latest versions of the UA string are at https://user-agents.net/applications/cfnetwork/platforms/ios
user_agent = "locationd/1753.17 CFNetwork/889.9 Darwin/17.2.0"
mac_address = re.compile(r"^[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}$")
session = None


def format_bssid(bssid):
    return ":".join(e.zfill(2) for e in bssid.split(":"))


def process_result(apple_wloc):
    device_locations = {}
    for wifi_device in apple_wloc.wifi_devices:
        if wifi_device.HasField("location"):
            lat = wifi_device.location.latitude * 1e-8
            lon = wifi_device.location.longitude * 1e-8
            bssid = format_bssid(wifi_device.bssid)
            if lat != -180 or lon != -180:
                device_locations[bssid] = {"bssid": bssid, "lat": lat, "lon": lon}
    return device_locations


def query_bssid_one(bssid):
    apple_wloc = AppleWLoc_pb2.AppleWLoc()
    wifi_device = apple_wloc.wifi_devices.add()
    wifi_device.bssid = bssid
    apple_wloc.unknown_value1 = 0
    apple_wloc.return_single_result = 1
    serialized_apple_wloc = apple_wloc.SerializeToString()
    length_serialized_apple_wloc = len(serialized_apple_wloc)

    data = b"\x00\x01\x00\x05"+b"en_US"+b"\x00\x13"+b"com.apple.locationd"+b"\x00\x0a"+b"8.1.12B411"+b"\x00\x00\x00\x01\x00\x00\x00" + bytes((length_serialized_apple_wloc,)) + serialized_apple_wloc
    r = session.post(api_endpoint, data = data)
    apple_wloc = AppleWLoc_pb2.AppleWLoc()
    apple_wloc.ParseFromString(r.content[10:])
    device_locations = process_result(apple_wloc)
    return device_locations.get(bssid)


def process_bssid(bssid, writer):
    bssid = bssid.lower()
    if not mac_address.match(bssid):
        print("Invalid BSSID", file = sys.stderr)
        return

    location = query_bssid_one(bssid)
    if location is not None:
        print(f"BSSID: {bssid}")
        print(f"Latitude: {location["lat"]}")
        print(f"Longitude: {location["lon"]}")
        print("")
        if hasattr(writer, "writerow"):
            writer.writerow((bssid, location["lat"], location["lon"]))
        elif writer is not None:
            print(f"BSSID: {bssid}", file = writer)
            print(f"Latitude: {location["lat"]}", file = writer)
            print(f"Longitude: {location["lon"]}", file = writer)
            print("", file = writer)
    else:
        print("The BSSID was not found.", file = sys.stderr)


def main():
    global session
    parser = ArgumentParser(description = "Check Apple wi-fi positioning database for the location of a BSSID")
    input_mode = parser.add_mutually_exclusive_group(required = True)
    input_mode.add_argument("-b", "--bssid", type = str, help = "display the location of the BSSID")
    input_mode.add_argument("-l", "--bssid-list", type = str, help = "Load list of BSSID from a file")
    parser.add_argument("-o", "--output-file", type = str, help = "Output file")
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})
    output = None
    writer = None
    header = ("bssid", "latitude", "longitude")
    if args.output_file is not None:
        output = open(args.output_file, "w", encoding = "utf-8")
        print(f"Writing {args.output_file}...", file = sys.stderr)
        if args.output_file.lower().endswith(".csv"):
            writer = csv.writer(output, delimiter = ",")
            writer.writerow(header)
        elif args.output_file.lower().endswith(".tsv"):
            writer = csv.writer(output, delimiter = "\t")
            writer.writerow(header)
        else:
            writer = output

    if args.bssid is not None:
        print(f"Querying for location of BSSID {args.bssid}...", file = sys.stderr)
        process_bssid(args.bssid, writer)
    elif args.bssid_list is not None:
        with open(args.bssid_list, "r", encoding = "utf-8") as input:
            i = 1
            for line in input:
                if line.startswith("#"):
                    continue
                bssid = line.rstrip()
                print(f"{i} Querying for location of BSSID {bssid}...", file = sys.stderr)
                process_bssid(bssid, writer)
                i += 1

    if args.output_file is not None:
        output.close()
    session.close()
    return 0


if __name__ == "__main__" or __name__ == "apple_bssid_locator":
    sys.exit(main())
