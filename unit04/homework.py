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

for transaction in transaction_lines:
    # insert new code here

# The most important keys for each transaction are:
# - transactionHash
# - blockTimestamp
# - address
# - direction
# - amount
# - name
# - category

# Question 1: Calculate the total amount sent by address TSHWYemZvVgxMJmMGWyNRkDFa46rvdboNs.
# Steps:
# - Identify the fields needed.
# - Construct a boolean expression to test whether a transaction line is relevant to answering the question.
# - Do the actual counting.

# Question 2: Calculate the total amount received by address TSHWYemZvVgxMJmMGWyNRkDFa46rvdboNs.
# - Hint: The code should be the same as for question 1, except for one change.

# Question 3: Print the transaction hashes for all transactions where the amount sent or received by address TSHWYemZvVgxMJmMGWyNRkDFa46rvdboNs is greater than or equal to 100,000.

# Question 4: The "cluster names" for each transaction is stored in the "name" key. Print the unique clusters from the data file, besides OKX.com.
