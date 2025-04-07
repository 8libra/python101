# Unit 9: Writing Native Excel Files

In this unit you will learn to:
- Install Python modules
- Generate native Excel files
- Determine when to use an AI model for help with Python

## 9.1 Modules: a review

*Modules* are packages of useful and reusable code that add extra functionality. Some modules are built into Python. Other modules need to be installed from the Internet. Regardless of the flavor, to use the module in our Python program we have to import it at the beginning of the program.

```python
import module_name
```

The modules that come with Python do a lot. These modules can check and send e-mail, read and write CSV files, do math, and much, much more. The modules that can be installed from the Internet can do even more, including plot graphs and run AI models. Truly, the imagination is the limit.

How does a developer know what module might help with a task? Experience, fellow developers and the Internet are good resources.

## 9.2 Installing Modules from the Internet

If we need to install a module from the Internet, we use the program `pip`:

```cmd
pip install module_name
```

## 9.3 Virtual Environments: a review

We generally run Python inside a virtual environment. To create a virtual environment, we run the command:

```cmd
python -m venv directory_name
```

To activate this virtual environment, we run the command:

```cmd
directory_name\scripts\activate.bat
```

One big reason we use virtual environments is because the modules installed in each virtual environment are separate. Installing module x in one virtual environment only installs module x in that one virtual environment. In complicated Python projects, sometimes modules may conflict with each other, or quite often a module depends on a very specific version of another module. A virtual environment is like a sandbox for the developer and the modules.

## 9.4 Install openpyxl

*openpyxl* is the Python module we will use to write native Excel files. Install this module into your Python environment with the command:

```cmd
pip install openpyxl
```

## 9.5 Why openpyxl?

The openpyxl module lets us write native Excel files with Python code. This can be very powerful. The openpyxl module has many features and can output hyperlinks, graphs and other advanced constructs. For our purposes, the big benefit of native Excel files is the ability to consolidate multiple worksheet tabs in a single Excel file, as opposed to sharing multiple text CSV files.

## 9.6 Basic but useful openpyxl flow

The way we use openpyxl is like this:

```python
import openpyxl # import the module to use it

wb = openpyxl.Workbook() # blank workbook
ws1 = wb.active # first worksheet object
ws1.title = "First worksheet title"
ws2 = wb.create_sheet("Second worksheet title")
ws3 = wb.create_sheet("Third worksheet title")

for row in list1:
    ws1.append(row)
for row in list2:
    ws2.append(row)
for row in list3:
    ws3.append(row)

wb.save("excel_filename.xlsx") # Finally, write the Excel file
```

## 9.7 How do we know what to do with a module?

The structure and syntax of a Python module is determined by its developers. To use the module, the users have to go with the developers' conventions -- or find a different module or write your own!

The quality of documentation varies. Some of these Python modules are maintained by very few people. And it may be the case that a useful module is one day abandoned by its developers and no longer updated.

Most popular modules have a homepage with documentation or examples. Asking fellow developers, using Google or using ChatGPT are other ways to get help.

## 9.8 A comment about ChatGPT and other AI models

One challenge with using ChatGPT and other similar AI tools is that the chat model can give false answers, called hallucinations. This tends to happen when the model doesn't really know the answer, but these models often do not know the strength or weakness of their knowledge.

An AI model's knowledge is based on its training data. If a model was trained on a lot of data about a particular subject, its knowledge on that subject tends to be good to great. If a model's training data did not include a lot of data about a subject, the model has a much higher chance to hallucinate.

For the topics covered in this course, using Python to manipulate data, the popular AI models have seen a lot of training data. Its knowledge and answers about these topics will generally be good. And, these models can often rephrase and explain things until the student gets it. ChatGPT is not a magic potion to learn Python, but it is a very, very useful tool.

You are encouraged to use ChatGPT or another AI model to continue your exploration of Python, or to get help.

Be aware of opsec, and clearly, do not send sensitive information into an online chat. But, if you want to know how to use Python to download a webpage, ChatGPT would provide a starting point. But, that is the topic of unit 10!

## 9.9 Homework

This unit's homework will be more self-directed than prior assignments. We can create an assignment together if you get stuck, but this homework is intended to encourage not just solving a problem, but defining a problem from scratch.

Find some data that you work with professionally that you feel can be usefully represented in a multi-tab Excel file. If this data is in one of the formats we have discussed, then you should have the ingredients to read the data and turn the data into an Excel file. On the other hand, if you feel another data source would be useful, then we can work together to try to use Python to read that data source.

Write a Python program to read in the data and make a multi-tab Excel file.

## 9.10 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- What modules are and how to install them
- How to use openpyxl to generate multi-tab Excel file
- Where to get help with Python, including AI tools
