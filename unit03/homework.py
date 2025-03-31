#! /usr/bin/env python
import csv

### DO NOT EDIT ###
transactions_data_file = "o1_transaction_log.csv"
transaction_lines = []
with open(transactions_data_file, "r", encoding = "utf-8") as input:
    reader = csv.reader(input)
    header = next(reader)
    for row in reader:
        transaction_line = dict(zip(header, row))
        # Values are read in as strings. But for the fields that represent numbers, we could convert the strings into numbers.
        transaction_line["blockHeight"] = int(transaction_line["blockHeight"])
        transaction_line["exchangeRate"] = float(transaction_line["exchangeRate"])
        transaction_line["trace#"] = int(transaction_line["trace#"])
        transaction_line["amount"] = float(transaction_line["amount"])
        transaction_lines.append(transaction_line)
### DO NOT EDIT ###

# Question 1: What is the type of the variable `transaction_lines`?

# Question 2: How many items are there in `transaction_lines`?

# Question 3: Pick one member from `transaction_lines`. What is the type of the member?

# The most important keys for each transaction are:
# - transactionHash
# - blockTimestamp
# - address
# - direction
# - amount
# - name
# - category

# initialize variables (lists, sets, dictionaries)

for transaction in transaction_lines:
    # insert new code here

# Question 4: Each transaction dictionary has a "transactionHash" key. Add each transactionHash key to a set. How many unique transaction hashes are in this dataset?

# Question 5: Each transaction dictionary has a "address" key. How many unique addresses are in this dataset?

# Question 6: Each transaction dictionary has a "amount" key. What is the total value of all of "amount"? Since sending and  receiving is logged separately, the amount calculated this way is generally counting the money twice.

# Question 7: Each transaction dictionary has an "amount" key. Using a set of list, what was the largest amount in the dataset?
