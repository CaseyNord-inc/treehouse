# Write a function named first_number that takes a string as an argument. The function should search, with a regular expression,
# the first number in the string and return the match object.

import re

def first_number(string):
    return re.search(r'\d', string)

# Now, write a function named numbers() that takes two arguments: a count as an integer and a string.
# Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.

def numbers(count, string):
    return re.search(r'\d' * count, string)