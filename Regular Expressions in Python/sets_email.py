# Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.

import re

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']

def find_emails(string):
    return(re.findall(r'[-\w\d+.]+@[-\w\d.]+', string))