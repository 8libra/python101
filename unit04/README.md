# Unit 4: Conditional Statements

In this unit you will learn to:
- Recognize expressions
- Think about True and False, computer style
- Use logic, comparison and membership operators
- Write conditional statements using if ... elif ... else

To start, launch a Python interactive shell.

## 4.1 Expressions

*Expressions* are Python code that calculate some result. They are a combination of variables, literal values, functions and operators. Examples:

- 4 # literally the number 4
- "hello" # literally the string hello
- x + y # assuming x and y were previously defined
- math.sqrt(9) # a number 3
- "spreadsheet.xlsx".endswith(".xlsx") # the boolean value True

We often save the value of an expression to a variable. But expressions can be used in other ways.

## 4.2 What are conditional statements?

Programming languages have a concept called conditionals. In English, this is saying, if some condition is true, run this code. Instead, if another condition is true, run that code. And if all else fails, if all the branches are false, run a third set of code.

Python has the bool type, which can be True or False.

```python
if True:
    print("Branch 1 code")
else:
    print("Branch 2 code")
```

Since the Boolean variable True is always true, the branch 1 code will always run. But we can use expressions and conditionals to do more interesting things.

We will come back to writing conditional statements in Python, but we first must understand boolean expressions.

## 4.3 Making Boolean Expressions

Clearly, the literal boolean value True is True, but we can write more sophisticated Boolean expressions using operators.

### 4.3.1 Comparison Operators

```python
l = [10, 20, 30]
print(len(l))
print(len(l) == 3) # True
print(len(l) != 3) # False!
```

We have comparison operators:
- == equality test
- != not equal test
- >, >=, <, <=

Each of these operators compares the left side of the expression with the right side of the expression, and returns True or False.

### 4.3.2 Membership Operators

```python
s = {1, 3, 5,3} # remember sets?
print(s)
print(3 in s) # True
print(9 in s) # False
print(3 not in s) # False
print(9 not in s) # True
```

### 4.3.3 Logical Operators

```python
print(not True) # False
t = False
print(not t) # True
```

Besides the *not* operator, we have *and* and *or*.

*and* evaluates to True if both sides of the expression are True, otherwise the expression evaluates to False.

*or* evaluates to True if one side or both sides of the expression are True, otherwise the expression evaluates to False.

## 4.4 Python's if statement

```python
if boolean_expression: # if True, run this branch
    # code
elif boolean_expression: # if no branch has run so far, check if this expression is True
    # code
elif boolean_expression: # if no branch has run so far, check if this expression is True
    # code
# ... can have many elif branches
else: # if all the Boolean tests have been False, run this branch
    # code
```

The if statement is looking for some expression that evaluates to a Boolean True or False, and executing the first branch of code where the Boolean expression evaluates to True. Note that *elif* branches and *else* branches are optional, depending on what the program needs.

```python
t = get_temperature() # this function is here as an example, there is no get_temperature() function
if t >= 115:
    print("It is very hot!")
```

```python
t = get_temperature() # this function is here as an example, there is no get_temperature() function
s = is_sunny() # this pretend function returns True or False
if t >= 115:
    print("It is very hot!")
elif t >= 70 and t <= 90 and s:
    print("It is nice outside!")
elif t <= 0:
    print("It is very cold!")
```

## 4.5 Homework Preparation

We will be using the same `o1_transaction_log.csv` file from the prior unit. We will be writing Python code to analyze the data in this file.

Guided task: Review the sourcecode of `homework.py`.

## 4.6 Homework

Open the file `homework.py` and complete the questions. Ask questions if stuck!

## 4.7 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Expressions
- Comparison operators
- Membership operators in, not in
- Logical operators not, and, or
- if ... elif ... else statement
