# Unit 2: Numbers and Lists

In this unit you will learn to:
- Store data in variables
- Call operators and functions
- Manipulate numbers and lists

To start, launch a Python interactive shell.

## 2.1 What are variables?

*Variables* are locations in computer memory that store data. Each variable has the following characteristics:
- A symbolic name
- A type
- A value

## 2.2 Assigning Values to Variables

In Python, the `=` operator sets a variable to a value. Examples:

```python
x = 100 # integer
pi = 3.14 # decimal, or floating point
print(type(x)) # prints <class 'int'>
print(type(pi)) # prints <class 'float'>
```

In Python, everything on a line after `#` denotes a *comment*.

## 2.3 Operators

We can do things with variables using *operators*.

```python
x = 100
y = x * 2 # multiplication
print(y)
y = x + 4 # addition
print(y)
x += 1 # shortcut for x = x + 1
print(x)
print(x == y) # test whether two values are equal
z = x == y
print(type(z)) # <class 'bool'>
```

*bool* is a variable type in Python that holds either True or False. The bool type will be useful in later units.

What are some other mathematical operators that could be in Python?

## 2.4 Functions

*Functions* are Python statements that do something. They may or may not return some value.

```python
print("The print function displays text and doesn't return anything.")
maximum = max(-5, 1, -3) # the max function does something and returns a value, which can be stored in a variable
help(max)
print(maximum)
```

Functions are called by writing the function name, followed by the function arguments in parenthesis.

Functions are like verbs in human language. Just like with human language, what functions are available and how to use them is something learned over time.

## 2.5 Lists

*Lists* hold an ordered collection of data. Duplicates are allowed.

```python
l = [0, 1, 2, 3, 4, 3.14]
print(type(l)) # <class 'list'>
print(l)
```

We can do useful stuff to lists with functions.

```python
l = [300, 400, 100, 500, 200] # initial list
print(l)
length = len(l)
print(length) # print and len are both functions!
l.append(600) # a different type of function called a method
print(l)
print(len(l)) # functions can be nested

l.sort(reverse = True) # sort list in descending order
print(l)
l.sort() # sort list in ascending order
print(l)

# more functions on lists
print(min(l))
print(max(l))
print(sum(l))
```

### 2.5.1 Accessing List Members and Slicing

```python
print(l[0]) # access individual members of a list; indices start from 0!
print(l[1])
print(l[-1])
l[1] = 900 # we can use indexing to modify a list too

new_list = l[3:5] # this is called a list slice
print(new_list)
print(type(new_list))

empty_list = [] # create an empty list
print(type(empty_list))
print(len(empty_list))
empty_list.append(9.25)
print(len(empty_list)) # no longer empty!
print(empty_list)
print(empty_list[0])
```

## 2.6 Homework Preparation

Guided task: Review the sourcecode of `make_random_numbers.py`. Note that in Python, code indentation is mandatory.

Guided task: Review the sourcecode of `homework.py`.

## 2.7 Homework

Open the file `homework.py` and complete the questions. Ask questions if stuck!

## 2.8 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Variables
- Several types of variables: int, float, list, bool
- Assignment operator
- Mathematical operators
- Equality operator
- Functions
- List indices and slicing
- Python comments
- Importance of indentation
