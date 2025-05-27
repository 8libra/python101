#! /usr/bin/env python

random_numbers_text_file = "random_numbers.txt" # a variable storing the name of the file that was created
# insert a line here to initialize an empty list
list_of_numbers = [] # empty list
with open(random_numbers_text_file, "r", encoding = "utf-8") as input: # open the file for reading
    for line in input: # read each line in the file
        # The variable `line` is a string with a newline at the end. The following line turns this line into the integer on that line.
        number = int(line.rstrip())
        # write a line here to store the `number` variable to the list you initialized, specifically append the number to the list.
        list_of_numbers.append(number)

# Question 1: How many numbers are in the file?
number_of_numbers = len(list_of_numbers) # we need this value for question 3
print(number_of_numbers)

# Question 2: What is the sum of all of the numbers in the file?
total = sum(list_of_numbers) # we need this value for question 3
print(total)

# Question 3: What is the average of the numbers? Hint: this will require use of one mathematical operator not explicitly covered in class.
average = total / number_of_numbers # / is the division operator
print(average)

# Question 4: What is the number on the 5000th line? Hint: the number on the first line is *not* stored at list index 1.
print(list_of_numbers[4999]) # remember list indices start at zero!

# Question 5: What is the number on the 599th line counting from the bottom?
print(list_of_numbers[-599]) # negative indices count from the end of a list, beginning with index -1

# Question 6a: Create a list slice (new list) of the numbers from the 401st to 500th line. Hint: watch the indices!
list_slice = list_of_numbers[400:500]

# Question 6b: Verify the length of this new list.
number_of_numbers = len(list_slice) # the prior value of total is thrown away, this is ok because we don't need the prior value anymore
print(number_of_numbers)

# Question 6c: Calculate the sum and average of this new list of numbers.
total = sum(list_slice) # the prior value of total is thrown away, this is ok because we don't need the prior value anymore
print(total)
average = total / number_of_numbers
print(average)

# Question 6d: Sort this list in ascending order. What is the tenth smallest value?
list_slice.sort()
print(list_slice[9])
