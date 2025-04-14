#! /usr/bin/env python
from random import randint # import a function called "randint" from a module called "random"

# Do not run this program, it will overwrite the existing file!
random_numbers_text_file = "random_numbers.txt" # a variable storing the name of the file to create
number_of_numbers = randint(10000, 10999) # the number of random numbers to make
with open(random_numbers_text_file, "w", encoding = "utf-8") as output: # create or overwrite the file
    for i in range(number_of_numbers): # do the following code "number_of_numbers" times
        a_random_number = randint(1, 100) # get a number from 1 to 100 inclusive
        string_to_write = str(a_random_number) + "\n" # \n represents a newline
        output.write(string_to_write)
