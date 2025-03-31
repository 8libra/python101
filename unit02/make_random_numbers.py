#! /usr/bin/env python
from random import randint

# Do not run this program, it will overwrite the existing file!
random_numbers_text_file = "random_numbers.txt" # a variable storing the name of the file to create
number_of_numbers = randint(10000, 10999) # the number of random numbers to make
with open(random_numbers_text_file, "w", encoding = "utf-8") as output: # create or overwrite the file
    for i in range(number_of_numbers):
        a_random_number = randint(1, 100)
        string_to_write = str(a_random_number) + "\n"
        output.write(string_to_write)
