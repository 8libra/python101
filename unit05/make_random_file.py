#! /usr/bin/env python
import csv
from random import randint

word_list_file = "word_list.tsv"
random_output_file = "random.txt"

words = []
with open(word_list_file, "r", encoding = "utf-8") as input:
    reader = csv.reader(input, delimiter = "\t")
    header = next(reader)
    for h, word1, word2 in reader:
        words.append(word1)
        words.append(word2)

# At this point, the list words contains 512 distinct random words.
with open(random_output_file, "w", encoding = "utf-8") as output:
    random_number = randint(1, 5120)
    while random_number > 0:
        if random_number % 10 == 8:
            output.write("\n") # blank line
        elif random_number % 10 == 9:
            output.write("# Skip this line\n") # comment line
        else:
            random_index = randint(0, 511)
            output.write(f"{words[random_index]}\n")
        random_number = randint(0, 5119)
