# Unit 7: Reading JSON Data

In this unit you will learn to:
- Recognize data stored in JSON format
- Load JSON data from a file into Python
- Practice analyzing a JSON file
- Practice analyzing a Python program written by someone else

## 7.1 What is JSON, and why do we care?

*JSON* stands for JavaScript Object Notation. It is a way to represent and share data. The reason we care is because JSON is widely used by services on the Internet to return data. JSON is not intended to be read by humans, but instead is intended to be parsed by computer programs.

We will see examples of data being returned in JSON format in unit 10. Suffice it to say, if an interface on the Internet is returning data that is intended to be used by a computer program, it is usually returned in JSON format.

## 7.2 Examples

```json
{
    "first_name": "Alan",
    "last_name": "Tu",
    "year_of_birth": 1981,
    "is_female": false,
    "pet": null
}
```

The braces denote a JSON *object*, which is analogous to Python dictionaries. Objects have keys, and each key has a value. Values can be a string, a number, a boolean or the value null.

There is one more data type in JSON, arrays which are the equivalent of Python lists, denoted by []. And nearly all real JSON on the Internet will have a multi-level nested structure.

```json
{
    "siblings":
    [
        {
            "name": "Alan",
            "city": "Las Vegas",
            "state": "CA",
            "country": "US",
            "is_female": false,
            "pet": null
        },
        {
            "name": "Kevin",
            "city": "Taipei",
            "state": null,
            "country": "TW",
            "is_female": false,
            "pet": null
        }
    ]
}
```

In words, the JSON above is an object. It has one key, *siblings*. The value of this key is an array. The array contains two objects describing a person. Each object contains several keys, which have corresponding values.

The layout of the data structure and the names of keys are up to the twisted imagination of the developer.

## 7.3 Reading JSON from a File

```python
import json

input_file = "fbi_cities1.json"
with open(input_file, "r", encoding = "utf-8") as input:
    data = json.load(input)
print(type(data))
```

In words, we first open a text file for reading, which gives us a file object. Then we run the json.load() function on the file object, and Python returns a Python variable which is a translation of the JSON data. This variable, called `data` above, can then be manipulated in Python.

## 7.4 A note on data structure

Please review the files `fbi_cities1.json` and `fbi_cities2.json` in a text editor. These two JSON files represent the exact same data, but use two different structures.

The choice of a structure is up to the person who created the program. Generally, if you are getting JSON from an API, the structure will be documented. But if you are getting a JSON file from a legal return, you will have to examine the structure manually and identify the data elements that you need.

## 7.5 Homework

### 7.5.1 Background

Obtain the file `google_drive.json` from me. This file was provided by Google and contains the audit trail for a Google Drive folder.

### 7.5.2 First program

Save the following program and run it:

```python
#! /usr/bin/env python
import json
import csv

json_file = "google_drive.json"
csv_file = "user_dictionary.csv"

with open(json_file, "r", encoding = "utf-8") as input:
    root = json.load(input)

with open(csv_file, "w", encoding = "utf-8") as output:
    writer = csv.writer(output)
    header = ["gaia_id", "email_address"]
    writer.writerow(header)

    for user in root["lis_metadata"]["activity_records"]["gaia_id_dictionary"]["user_info"]:
        row = [user["user"]["gaia_id"], user["user"]["email_address"]]
        writer.writerow(row)
```

Questions:
1. What file is created?
2. What is in the output file?
3. What is the program doing to generate the output?
4. Use a text editor to open google_drive.json. Can you find the fields that the output came from?

### 7.5.3 Second program

Review the following program and answer the questions:

```python
#! /usr/bin/env python
import json
import csv

json_file = "google_drive.json"
csv_file = "activity_records.csv"

with open(json_file, "r", encoding = "utf-8") as input:
    root = json.load(input)

with open(csv_file, "w", encoding = "utf-8") as output:
    writer = csv.writer(output)
    header = ["time", "gaia_id"]
    writer.writerow(header)

    data = []
    for activity_record in root["lis_metadata"]["activity_records"]["activity_event_records"]:
        row = [activity_record["time"], activity_record["actor"]["user"]["unknown_user"]["gaia_id"]]
        data.append(row)

    data.sort()
    for row in data:
        writer.writerow(row)
```

Questions:
1. What is this program doing?
2. What would be in the output file?
3. What is the purpose of the `data.sort()` line?
4. Use a text editor to open google_drive.json. Can you find the fields that the output came from?

You may save and run the program if you wish.

## 7.6 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- What JSON is and where it is used
- JSON data types and how they are written: numbers, strings, Boolean, null, arrays and objects
- How JSON data types relate to Python data types
- How to load JSON data stored in a file into Python
