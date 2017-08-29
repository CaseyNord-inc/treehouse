# Import the Challenge class from models.py.

from models import Challenge

# Now, create a variable named all_challenges. It should select all of the available challenges from the database.

all_challenges = Challenge.select()

# Next, create a new Challenge. The language should be "Ruby", the name should be "Booleans".

Challenge.create(language="Ruby", name="Booleans")

# Finally, make a variable named sorted_challenges that is all of the Challenge records,
# ordered by the steps attribute on the model. The order should be ascending, which is the default direction.

sorted_challenges = Challenge.select().order_by(Challenge.steps)