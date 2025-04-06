# Unit 6: Reading and Writing CSV and TSV Files

In this unit you will learn to:
- Open a file to read textual data
- Open a file to write textual data
- Read CSV files
- Write CSV files

## 6.1 Why files?

*Files* contain data we want to analyze, and we can save results of analysis in files to share with others. We will be learning to read from and write to files on disk.

## 6.2 File Operations

There are many different types of file operations. There are separate flavors for reading and writing files that contain textual data (CSV, JSON, HTML) and reading and writing files that contain binary data (ZIP files, images, PDF files, Microsoft Office files.)

In this unit, we will focus on reading textual files and writing textual files.

## 6.3 Opening Files for Reading and Writing

```python
with open(filename, "r", encoding = "utf-8") as input:
    # `input` is called a file handle
    # filename is a string
    # code that uses the file must be indented
```

```python
with open(filename, "w", encoding = "utf-8") as output:
    # filename is a string
    # code that uses the file must be indented
```

```python
with open(in_file, "r", encoding = utf-8") as input, open(out_file, "w", encoding = "utf-8") as output:
    # code that uses the files must be indented
```

Explanation:
- The *with* keyword is what Python calls a context manager. This is the recommended form to open files.
- The `open` function has several arguments. The first argument is the filename. The second argument is the *mode*, "r" for reading text files and "w" for writing text files. The `encoding = "utf-8"` argument enables correct reading and writing of international characters. Some returns may have text in foreign languages!

## 6.4 Simple Examples

### 6.4.1 Simple copy program

```python
in_file = "in.txt" # file must exist
out_file = "out.txt" # if the file exists, it will be overwritten

with open(in_file, "r", encoding = utf-8") as input, open(out_file, "w", encoding = "utf-8") as output:
    # Read each line of input in a loop
    for line in input:
        output.write(line)
```

### 6.4.2 Comment out each line

```python
in_file = "in.txt" # file must exist
out_file = "out.txt" # if the file exists, it will be overwritten

with open(in_file, "r", encoding = utf-8") as input, open(out_file, "w", encoding = "utf-8") as output:
    # Read each line of input in a loop
    for line in input:
        new_line = "# " + line
        output.write(new_line)
```

If both `x` and `y` are string expressions, the `+` operator concatenates them.

## 6.5 CSV and TSV Files

*CSV* files are comma-separated-value files and are one common type of data. *TSV* files, less common, are tab-separated-value files. Both files contain a record or row on each line. The record or row on each line contain multiple fields, separated by a delimiter. CSV files use the delimiter ",", and TSV files use the delimiter tab which in Python is represented by "\t".

If a header exists in the file, it is the first row.

The advantage of CSV files is that they are automatically recognized by Excel. CSV files are not actually native Excel files, but many people don't realize the difference.

The advantage of the less common TSV files is that they more cleanly accommodate data that has commas in the actual fields.

One downside of both CSV and TSV files is that they cannot support separate worksheets in the same file. To store multiple worksheets in the same file, we need to use a native Excel file.

## 6.6 Reading a CSV or TSV File

```python
import csv # The `csv` module comes with Python

in_file = "data.csv"
with open(in_file, "r", encoding = utf-8") as input:
    reader = csv.reader(input)
    # At this point, the variable `reader` is a magic object that is set up to make reading rows and fields easy.
    header = next(reader) # if the first line is a header
    for row in reader:
        # `header` and `row` are lists of values that can be read and manipulated
```

```python
import csv # The `csv` module comes with Python

in_file = "data.tsv"
with open(in_file, "r", encoding = utf-8") as input:
    reader = csv.reader(input, delimiter = "\t")
    # At this point, the variable `reader` is a magic object that is set up to make reading rows and fields easy.
    header = next(reader) # if the first line is a header
    for row in reader:
        # `header` and `row` are lists of values that can be read and manipulated
```

## 6.7 Writing a CSV or TSV File

```python
import csv # The `csv` module comes with Python

out_file = "data.csv"
with open(out_file, "w", encoding = utf-8", newline = "") as output:
    # The newline = "" argument is needed to prevent duplicate newline characters at the end of each row
    writer = csv.writer(output)
    # At this point, the variable `writer` is a magic object that is set up to make writing rows and fields easy.
    header = ["list", "of", "columns"]
    writer.writerow(header)
    # loop over something
        # construct row, a list of fields in a row
        writer.writerow(row)
```

```python
import csv # The `csv` module comes with Python

out_file = "data.tsv"
with open(out_file, "w", encoding = utf-8", newline = "") as output:
    # The newline = "" argument is needed to prevent duplicate newline characters at the end of each row
    writer = csv.writer(output, delimiter = "\t")
    # At this point, the variable `writer` is a magic object that is set up to make writing rows and fields easy.
    header = ["list", "of", "columns"]
    writer.writerow(header)
    # loop over something
        # construct row, a list of fields in a row
        writer.writerow(row)
```

The key point here is that `writer.writerow()` takes a list of values and uses the `writer` magic object to correctly write the values to the file.

## 6.8 A real world example: convert.py

convert.py is a Python program that converts between CSV files and TSV files.

```python
#! /usr/bin/env python
import sys
import csv

if len(sys.argv) != 3:
    print("Usage: python convert.py <input_file> <output_file>", file = sys.stderr)
    sys.exit(1)
input_file, output_file = sys.argv[1], sys.argv[2]
# `sys.argv` is a list variable that contains arguments specified at the command line, the first argument is at index 1 because index 0 is the name of the Python file
# sys.stderr is a way to print error messages to the screen, and is used to distinguish between error and status messages and data output
# sys.exit is a function that exits Python, with an status code

# Detect input delimiter using the filename extension
# we use the lower() function because the case of the filename is unpredictable
if input_file.lower().endswith(".csv"):
    input_delimiter = ","
elif input_file.lower().endswith(".tsv"):
    input_delimiter = "\t"
else:
    print("Input delimiter could not be determined, exiting.", file = sys.stderr)
    sys.exit(2)

# Detect output delimiter using the filename extension
# we use the lower() function because the case of the filename is unpredictable
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
```

## 6.9 Homework

The `o1_transaction_log.tsv` file is the same list of blockchain transactions we have worked with previously, except that the file is a TSV file, *not* a CSV file.

Open and read the `o1_transaction_log.tsv` file. The first line is the header, and should not be treated as data.

The 11th field of each row (*not* index 11) contains the Chainalysis cluster name, or the empty string "". The first and fourth fields of each row contain the transaction hash and timestamp respectively, again watch the indices!

Loop through the rows. Output a new CSV file (comma-separated-value) writing the transaction hash, timestamp and cluster name if:
- The cluster name is not the empty string "", *and*
- The cluster name is not "OKX.com"

## 6.10 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Opening text files for reading and writing
- The difference between CSV files and TSV files
- Reading from and writing to a CSV or TSV file
