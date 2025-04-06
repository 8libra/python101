#! /usr/bin/env python

random_output_file = "random.txt"

with open(random_output_file, "r", encoding = "utf-8") as input:
    # start here
    # Assignment:
    # (a) Read each line in a loop.
    # (b) Use the .rstrip() function to return a new string that has the newline character removed
    # Each line has four possibilities:
    # (1) A blank line, which can be checked for by comparing len(...) == 0 or by checking if the stripped line is equal to the empty string ""
    # (2) A line that .startswith("#") returns True
    # (3) an actual word, other than "racketeer"
    # (4) the stop word "racketeer"

    # The assignment is to identify the line number, **excluding blank lines and comment lines**, of the first use of the stop word "racketeer"
    # (c) Write code that handles each of the four possibilities
    # Hints:
    # Use a conditional statement if ... elif ... else.
    # Possibility (1) and (2) can be handled using the same conditional branch. Use a boolean expression to check for both possibilities. In these cases we want to do nothing else with that line.
    # For possibility (3), we want to keep track of the line number.
    # For possibility 4, we should exit the loop

# At this point, we have exited the loop. We should have kept track of the appropriate line number, and can use the print() statement to print that variable.
