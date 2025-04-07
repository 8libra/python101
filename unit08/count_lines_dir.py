#! /usr/bin/env python
# We need some modules.
import os
import sys


# Our prior counting lines function
def count_lines(text_filename):
    lines = 0
    with open(text_filename, "r", encoding = "utf-8") as input:
        for line in input:
            lines += 1
    return lines


if len(sys.argv) != 2: # no command line argument was provided, exit with message
    print("Usage: python count_lines_dir.py <directory>", file = sys.stderr)
    sys.exit(1)

text_file_extensions = [".txt", ".md", ".py", ".json", ".csv", ".tsv"]
dir_list = os.listdir(sys.argv[1]) # Get list of filenames and folder names ...
dir_list.sort() # ... and sort it

for dir_entry in dir_list: # iterate over the list
    full_path = os.path.join(sys.argv[1], dir_entry) # concatenate the directory name with the filename
    if not os.path.isfile(full_path): # if the directory entry is not a file (like a folder)
        continue # skip it

    file_basename, file_extension = os.path.splitext(dir_entry.lower())
    if file_extension not in text_file_extensions: # not one of the extensions we want
        continue

    lines = count_lines(full_path)
    print(f"{full_path}: {lines} lines") # print using an f-string
