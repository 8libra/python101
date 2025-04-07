# Unit 1: Setup and First Program

In this unit you will learn to:
- Set up the software environment for future learning
- Write, save and run your first Python program
- Run Python programs supplied by others

## 1.1 Install Programs

Guided task: Download and install the following programs:
- [Python](https://www.python.org/downloads/)
- [Notepad++ text editor](https://notepad-plus-plus.org/downloads/v8.7.8/)
- [Git version control](https://git-scm.com/downloads/win)

## 1.2 Python Setup

Guided tasks:
- Create a desktop shortcut to Command Prompt `C:\Windows\System32\cmd.exe`
- Create a Python virtual environment called main with the command `python -m venv main`
- Create a batch file to launch the main virtual environment

## 1.3 First Steps into Python

Guided tasks:
- Launch a *Python interactive shell* with `python -i`
- Run statements and exit
- Use Notepad++ and save the following Python program:

```python
#! /usr/bin/env python
print("Hello, World!")
```

- Run the program

## 1.4 Homework Preparation

Python programs often require extra reusable code, called *modules*. There are two flavors of modules: modules that come with Python and modules that do not come with Python. For the modules that don't come with Python, we use the program `pip` to install these modules.

Guided tasks:
1. Upgrade pip to ensure it is the latest version.

```cmd
pip install -U pip
```

2. Install the two extra modules required by the program used in the homework:

```cmd
pip install requests protobuf
```

3. Use `git` to download the files needed for the homework.

```cmd
git clone https://github.com/8libra/python101.git
```

## 1.5 Homework

1. Use the `cd` command to change into the apple_bssid_locator directory. Run the `apple_bssid_locator.py` program:

```cmd
python apple_bssid_locator.py -b 04:d9:f5:fa:d4:fc
```

What is the latitude and longitude returned?

2. Create a text file using Notepad++ with each line containing a BSSID. Save the text file. Then run:

```cmd
python apple_bssid_locator.py -l text_file -o bssid_info.csv
```

## 1.6 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Virtual environments
- Python interactive shell
- Modules
- Cross platform code
