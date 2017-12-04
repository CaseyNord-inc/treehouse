# Create a function named phone_numbers that takes a string and returns all of the phone numbers in the string using re.findall().
# The phone numbers will all be in the format 555-555-5555.

import re

def phone_numbers(string):
    return re.findall(r'\d{3}-\d{3}-\d{4}', string)