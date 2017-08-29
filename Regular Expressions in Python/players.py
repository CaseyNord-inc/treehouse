# Create a variable named players that is an re.search() or re.match()
# to capture three groups: last_name, first_name, and score. It should include re.MULTILINE.

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'^(?P<last_name>[\w\s?]+),\s(?P<first_name>[\w\s?]+): (?P<score>\d+)$', string, re.M)

# Wow! OK, now, create a class named Player that has those same
# three attributes, last_name, first_name, and score. I should be able to set them through __init__.

class Player:
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score