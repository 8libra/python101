# Unit 3: Strings, Sets and Dictionaries

In this unit you will learn to:
- Use Python strings, sets and dictionaries

To start, launch a Python interactive shell.

## 3.1 Strings

*Strings* are a variable type that contains text,which can include international characters (Unicode.) Strings can represent important data such as IP addresses or cryptocurrency addresses.

```python
s1 = "Hello, World!"
print(s1) # strings can be printed
sentence = "This sentence contains several words."
list_of_words = sentence.split(" ") # and split
print(type(list_of_words))
print(len(list_of_words))
print(list_of_words)

list_of_words = ["Construct", "a", "new", "sentence."]
new_string = " ".join(list_of_words)
print(new_string)

filename = "SPREADSHEET.XLSX"
print(filename.lower())
print(filename) # The variable filename was not changed by the function.
print(filename.lower().endswith(".xlsx")) # True

# Here, the token \n represents a newline
# Generally, when we read text from a file, each line will end in a newline
# We often want to remove this.
simulated_line = "IP: 1.2.3.4\n"
print(simulated_line)
data = simulated_line.rstrip()
print(data)
```

## 3.2 Sets

A *set* is a variable type that is similar to lists, meaning it holds several bits of data. Unlike lists, sets are not ordered, and adding a duplicate value to a set has no effect.

```python
s = set() # empty set
print(type(s)) # <class 'set'>
print(len(s))
s.add(1)
print(s)

list_of_numbers = [4, 2, 5, 3, 1, 4, 9, 25, -1, 3, 25, 4]
s = set(list_of_numbers) # make a set from a list!
print(s)
print(len(s))

s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
s3 = s1.intersection(s2) # set intersection
print(s3)
s4 = s1.union(s2) # set union
print(s4)
s5 = s2 - s1 # set subtraction
print(s5)
```

## 3.3 Dictionaries

A *dictionary* stores keys and associated values. Keys and values can be any variable type.

```python
my_characteristics = {
    "first_name": "Alan", # string
    "last_name": "Tu",
    "is_female": False, # boolean
    "age": 43, # integer number
    "height_in_meters": 1.75 # floating point number
}
print(my_characteristics["age"])
my_characteristics["state"] = "NV"
print(my_characteristics)
```

## 3.4 Homework Preparation

Guided task: Review the sourcecode of `make_random_numbers.py`. Note that in Python, code indentation is mandatory.

Guided task: Review the sourcecode of `homework.py`.

## 3.5 Homework

Open the file `homework.py` and complete the questions. Ask questions if stuck!

## 3.6 Important Concepts

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
