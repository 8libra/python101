# Unit 8: Functions, Command Line Arguments and Directory Operations

In this unit you will learn to:
- Write functions
- Process command line arguments
- Process multiple files in a directory

## 8.1 What are functions?

*Functions* in Python are blocks of reusable code. Functions accept zero or more parameters, run code, and optionally return values.

Here are some example functions:

```python
def print_hello(): # no parameters
    print("Hello. I am a boring function.")
    # no return values

print_hello()
print_hello()
```

```python
def print_greeting(name):
    print(f"Hello {name}. I am a slightly less boring function.")

print_greeting("Brendan")
x = "Alan"
print_greeting(x)
```

```python
def square_me(x):
    return x * x

y = square_me(2)
print(y)
```

```python
def square_cube_me(x):
    return x*x, x*x*x

a, b = square_cube_me(2)
print(a)
print(b)
```

```python
def add_first_two(l):
    return l[0] + l[1]
```

Key points:
- Functions take zero or more parameters. Each parameter can be of any type: numbers, strings, lists, sets, dictionaries, types we haven't covered.
- Functions operate on the parameters and run some code, and return zero or more values.
- The author of the function and the user calling the function must have a common understanding of the function's parameter and return value conventions.

## 8.2 Counting Lines in a Text File

Sometimes we get a large log file or CSV spreadsheet and we just want to know the number of lines in this file. We can write our line counting code in a function, like this:

```python
def count_lines(text_filename):
    lines = 0
    with open(text_filename, "r", encoding = "utf-8") as input:
        for line in input:
            lines += 1
    return lines
```

We don't have to write a function. But writing this function lets us call this block of code without rewriting the same code over and over again for each different file.

## 8.3 Command Line Arguments

We often want to let the user give the Python program some dynamic variable, such as the BSSID to query in our apple_bssid_locator.py program. These are called *command line arguments*.

```cmd
python my_program.py argument_1 argument_2
```

For "simple cases", we can use the `sys.argv` mechanism to access the user supplied arguments, if any, from inside the Python program.

```python
import sys # required!

print(type(sys.argv)) # list
print(sys.argv)
```

If we `import sys`, the sys.argv list variable will be available. The list will always have at least one value, the name of the program at index 0. If there are any command line arguments, they will start at index 1.

## 8.4 Processing Multiple Files in a Directory

What if we want to do *something* to all the files in a directory? We will be reviewing this code together in detail.

```python
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
```

Ideas from prior units:
- Importing modules for additional functionality
- `sys.argv` is a list variable that includes the command line arguments entered by the user, if any. List index 0 is the name of the program so anything provided by the user starts at index 1.
- `l.sort()` where l is a list, sorts the list.
- `s.lower()` where s is a string, creates a new string except that all the letters are lowercase.
- f-strings, or formatted string literals
- Some functions are in the form function_name(variable), like `os.listdir(directory_name)`, while other functions are in the form variable.function() like `string.lower()`. The latter are technically *methods* that operate on objects. Think of the different forms of functions as different types of verbs, you will learn them with experience.

New ideas:
- The function `os.listdir(directory_name)` returns a list of file and subdirectory names. This list is not sorted, so if we want to process the files in alphabetical order, we must sort that list ourselves.
- The function `os.path.isfile(name)` returns True if the name is a file, and returns False if the name is not a file (such as if it is a folder.)
- The function `os.path.splitext(filename)` splits the filename into the base filename and the file extension. This function returns two values.
- Function calls can be nested.

## 8.5 Homework

We have transaction log data for two Tether on Tron cryptocurrency addresses of interest:
- TAgEaCZGoReTs5WtKTbzDoVYMyioYCF4os_transaction_log.tsv
- TSHWYemZvVgxMJmMGWyNRkDFa46rvdboNs_transaction_log.tsv

The objective is to identify any addresses that these two addresses have in common.

1. Write code to open one of the TSV files. Use the `csv` module, but note that the delimiter is tab, or "\t" in Python.
2. Iterate over the rows in the file. The address field in each row is the eight field (not index 8!) For each row, add the address value to a set.
3.  Change the code into a function. The function will take one parameter, the filename. The function will iterate over the file and return the set containing the addresses found in that file.

Outside the function, call the function for each file. We should have two sets, which could be called `s1` and `s2`. The set of addresses that both wallets have in common can be found with:

```python
common_addresses = s1.intersection(s2)
for address in common_addresses: # print nicely
    print(address)
```

What are the common addresses found in these transaction logs? These are leads for further investigation!

## 8.6 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Functions, parameters and return values
- Command line arguments and how to access them
- Processing files in a directory
