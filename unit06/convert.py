#! /usr/bin/env python
import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python convert.py <input_file> <output_file>", file = sys.stderr)
    sys.exit(1)
input_file, output_file = sys.argv[1], sys.argv[2]

if input_file.lower().endswith(".csv"):
    input_delimiter = ","
elif input_file.lower().endswith(".tsv"):
    input_delimiter = "\t"
else:
    print("Input delimiter could not be determined, exiting.", file = sys.stderr)
    sys.exit(2)

if output_file.lower().endswith(".csv"):
    output_delimiter = ","
elif output_file.lower().endswith(".tsv"):
    output_delimiter = "\t"
else:
    print("Output delimiter could not be determined, exiting.", file = sys.stderr)
    sys.exit(4)

with open(input_file, "r", encoding = "utf-8") as input, open(output_file, "w", encoding = "utf-8", newline = "") as output:
    print(f"Reading from {input_file}...", file = sys.stderr)
    print(f"Writing to {output_file}...", file = sys.stderr)
    reader = csv.reader(input, delimiter = input_delimiter)
    writer = csv.writer(output, delimiter = output_delimiter)
    for row in reader:
        writer.writerow(row)
