# Import OrderedDict from the collections module.

from collections import OrderedDict

## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'

# Now create an OrderedDict named menu that has the menu items exactly as listed in the comment.
# Both keys and values will be strings.

menu = OrderedDict([
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge')
])