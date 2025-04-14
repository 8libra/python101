#! /usr/bin/env python

random_numbers_text_file = "random_numbers.txt" # a variable storing the name of the file that was created
# insert a line here to initialize an empty list
with open(random_numbers_text_file, "r", encoding = "utf-8") as input: # open the file for reading
    for line in input: # read each line in the file
        # The variable `line` is a string with a newline at the end. The following line turns this line into the integer on that line.
        number = int(line.rstrip())
        # write a line here to store the `number` variable to the list you initialized, specifically append the number to the list.

# Question 1: How many numbers are in the file?

# Question 2: What is the sum of all of the numbers in the file?

# Question 3: What is the average of the numbers? Hint: this will require use of one mathematical operator not explicitly covered in class.

# Question 4: What is the number on the 5000th line? Hint: the number on the first line is *not* stored at list index 1.

# Question 5: What is the number on the 599th line counting from the bottom?

# Question 6a: Create a list slice (new list) of the numbers from the 401st to 500th line. Hint: watch the indices!

# Question 6b: Verify the length of this new list.

# Question 6c: Calculate the sum and average of this new list of numbers.

# Question 6d: Sort this list in ascending order. What is the tenth smallest value?
