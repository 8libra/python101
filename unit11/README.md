# Unit 11: A Dip into Regular Expressions and Capstone

In this unit you will learn to:
- Understand what regular expressions are
- Recognize when they might be useful
- Use a basic regular expression workflow

## 11.1 Introduction to Regular Expressions

*Regular expressions*, often called *regex*, are a concise way to describe patterns in text. They let you specify a search pattern to quickly locate, match, or extract pieces of text from a larger body of text. This is especially useful when you're dealing with unstructured or messy text. In Python, the `re` module provides functions to apply these patterns, enabling you to locate, match, extract and replace (not covered here) parts of the text. Learning regex gives you a powerful, general-purpose tool for a variety of text processing tasks that you might encounter.

## 11.2 Workflow

The scenario for using regular expressions is that we have some text stored as a Python string, and we want to check if the string matches a pattern, or extract part of the string. The workflow for doing this is:
1. Write a regular expression that specifies what is supposed to be matched, found or extracted.
2. Compile the regular expression.
3. Call the operation.
4. Check the result.

Step 1 is the most difficult. Regular expressions use a specialized language that is very terse and compact. We will only be covering some of the capabilities of regular expressions and scratching the surface here. But if you have a task with messy, unstructured text, you should ask whether regular expressions can help.

## 11.3 Regular Expressions by Example

For the example regular expressions, we will be using the example string

Mary had a little lamb.

Regular expressions (regex) are strings, with their own specialized language.

The regex `Mary` matches the first part of the string.

The regex `x` does not match because there is no x in the string.

The regex `h.d` matches on had. . represents any single character. . is an example of a *metacharacter* and a *quantifier*.

The regex litle does not match.

The regex lit*le matches. * is another quantifier that says the preceding character can match 0 or more times.

The regex lit+le matches. + is another quantifier that says the preceding character can match 1 or more times.

The regex lit?le does not match. ? is another quantifier that says the preceding character can match 0 or 1 times.

The regex (l.*le) matches. Let's break this down:
- . matches any single character.
- The * indicates we want to match the prior character (which is any character) zero or more times.
- Is there any part of the string that fits? Yes, the word little.
- The parentheses captures, or extracts, that particular text. It is available to us. This is called a *capture group*.

## 11.4 How to Use Regex in Python

```python
import re # import the re module, which comes with Python

text = "Mary had a little lamb."
p = re.compile(regex_string, flags) # we will discuss one flag in the exercise
# think of p as a pattern object
m = p.search(text)

# At this point, m is either a match object or None. A match object is considered True, and None is considered False, so we can do this:
if m:
    # At this point, we know there is a match.
    # Access the capture groups we defined, if we defined any
    first_capture_group = m.group(1) # if any
    second_capture_group = m.group(2) # if any
    # there is a m.group(0) but we don't want that value.
else:
    # At this point, we know the regex did not match.
```

## 11.5 Capstone Exercise

This capstone exercise will combine many of the skills learned in prior units. You will almost certainly have to review examples from prior units. Do not use ChatGPT or any chatbot or coding assistant.

### 11.5.1 Specification

This specification is daunting, but I will guide you by breaking the problem down into smaller parts. With the exception of two more features of regex, you have learned everything you need to solve this problem.

You will write a Python program that takes two command line arguments. The first argument is a text file with a list of URLs. The second argument is a CSV or Excel file where the output will be stored.

For the file listing the URLs, lines starting with # or blank lines should be ignored.

For each URL, the program will download the URL and store the following three fields:
- The URL
- The HTTP response code
- The HTML title, the part of the web page (if the URL is a web page) between the <title> and </title> tags

The output will be in one of three formats, depending on the filename extension:
- .csv: CSV file
- .tsv: tab-separated-values file, just like CSV but with a different delimiter
- .xlsx: Excel spreadsheet

## 11.5.2 Planning

Before I guide you through each part, take at least 10 minutes to try to outline a structure for your code.

Do not read the guided part below until spending at least 10 minutes brainstorming a structure.

## 11.5.3 Function: Extracting the HTML Title

This is a function that takes a string as a parameter, and uses regex to extract the HTML title, if any.

```python
def extract_html_title(html):
    p = re.compile("<title>(.+?)</title>", re.I)
    m = p.search(html)
    if m:
        return m.group(1)
    else:
        return None
```

Wait, what is this?
- The second, and optional, parameter to re.compile are flags. The most useful flag is re.I, which tells the regex engine to ignore the case. It makes the regex case insensitive.
- The .+? is a modified quantifier. .+ matches any character one or more times, stopping at the closing HTML tag. But by default, regex quantifiers are greedy and match as much text as they can. This should not be a problem with HTML titles because there is probably only one HTML title tag. But if you were trying to analyze an HTML tag that occurred several times, greedy matching would be a problem. The match would start at the first occurrence of the HTML tag, which may be OK, but the match would end at the last occurrence of the HTML tag, which is probably not what you want. The ? modification tells the engine to match as little as possible.
- `None` is a valid value in Python and can mean null or empty. In Boolean expressions, None is the same as False.

## 11.5.4 Function: Handle each URL

The input parameter to this function should be a single URL.

Download the URL and note the HTTP response code.

Call the provided function to extract the HTML title, which could return None.

Return a list with the above two values.

## 11.5.5 Main program

First, we will need to import the modules we will need. The program will need to write CSV files, write Excel files, talk to web servers and operate on regular expressions. There could be other imports needed too.

Next, we should check that we have two command line arguments. If not, we should warn the user and exit.

Next, we need to open the text file for reading and iterate through the lines in a loop. For each line, we need to strip off the trailing newline character. We should use a conditional and a Boolean expression to check whether the line starts with a comment character # or is a blank line, and move on if it does.

For each URL, we should call the handle URL function. That function returns a list of two values: the HTTP response code, and the HTML title string. Create a list of three values: the URL, the HTTP response code and the HTML title. Then append this list to a running list.

At this point, you have collected your data. You have a list, with each member of that list being itself a list of three values. We now need to output the data.

Use logic to decide the output format depending on the file extension of the second command line argument.

Write code to output each of the three formats, including a header line.

Consider putting the code to output each format into separate functions. But, could the same function handle both CSV and TSV output?

## 11.6 Discussion

Let's review the capstone together, discuss potential optimizations and reflect on what we have achieved.

## 11.7 Important Concepts

Ensure you understand the following concepts (if not, ask!):

- Regular expressions
- Quantifiers
- Capture groups
- The value `None` in Python
