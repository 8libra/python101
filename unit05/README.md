# Unit 5: Loops

In this unit you will learn to:
- Recognize and employ various types of loops

## 5.1 What are loops?

*Loops* are used to execute a section of code multiple times.

```python
# Without loops
print(0)
print(1)
print(2)
print(3)
print(4)

# with loops
for i in range(5):
    print(i)
```

## 5.2 Types of Loops

### 5.2.1 Do something some number of times

```python
for i in range(number_of_times):
    print(i)
```

### 5.2.2 Do something for each value in a list or "similar structure"

```python
text = "These are the words in a sentence."
list_of_words = text.split(" ")
print(list_of_words)

for word in list_of_words:
    print(f"The word is {word}.")

s = {"Dick", "Tom", "Harry"} # a set
for name in s:
    print(s)

my_characteristics = {"first_name": "Alan", "last_name": "Tu", "state": "NV"}
for k in my_characteristics.keys():
    print(k)
```

### 5.2.3 Do something for each line in a text file

```python
with open(filename, "r", encoding = "utf-8") as input:
    print(type(input))
    for line in input:
        print(line)
```

### 5.2.4 Do something, and have available the index while doing it

```python
long_list = [1, 49, 29, 66, -1, -4, 2, 29, 49, -39, 37, 111]
for i, value in enumerate(long_list):
    print(f"The value at index {i} is {value}.")
```

### 5.2.5 Go through a dictionary, with the key and value available

```python
my_characteristics = {"first_name": "Alan", "last_name": "Tu", "state": "NV"}

for k, v in my_characteristics.items():
    print(f"{k}: {v}")
```

### 5.2.6 While Loop

The while construct is used when we want to continue a loop when a specified boolean expression is True, and stop the loop when that expression is False.

```python
count = 1
while count <= 10:
    print(count)
    count += 1
```

## 5.3 continue

The *continue* keyword in a loop skips this particular iteration of the loop and goes to the next iteration.

```python
l = [1, 2, 3, 4, 5]

for number in l:
    if number == 3:
        continue
    print(number)
```

## 5.4 break

The *break* keyword in a loop stops running the loop.

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in l:
    if number == 4:
        break
    print(number)
```

## 5.5 Homework Preparation

Guided task: Review the sourcecode of `make_random_file.py`.

Guided task: Review the sourcecode of `homework.py`.

## 5.6 Homework

Open the file `homework.py` and complete the assignment. Ask questions if stuck!

## 5.7 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- for loops
- while loops
- break and continue
