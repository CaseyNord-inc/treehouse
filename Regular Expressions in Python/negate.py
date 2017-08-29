# Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except the numbers 5, 6, and 7.

import re

string = '1234567890'

good_numbers = re.findall(r'[^567]', string)