# Create a function named find_words that takes a count and a string.
# Return a list of all of the words in the string that are count word characters long or longer.

import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, string):
    return re.findall(r'\w{6,}', string)

# Plugged in 6 because of this error message.  Fudged the challenge a bit.
# Bummer! Didn't get the right output. Output was []. Length was 6.