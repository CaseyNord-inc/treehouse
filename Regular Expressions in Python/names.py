# Create a variable names that is an re.match() against string.
# The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'(?P<lastname>\w+), (?P<firstname>[\w ]+)', string)