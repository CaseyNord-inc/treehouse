import re

# Use open() to load the file "basics.txt" into the variable file_object.

file_object = open("basics.txt")

# Read the contents of file_object into a new variable named data.

data = file_object.read()

# Now close the file_object file so it isn't taking up memory.

file_object.close()

# Import re. Create an re.match() for the word "Four" in the data variable. Assign this to a new variable named first.

first = re.match(r'Four', data)

# Finally, make a new variable named liberty that is an re.search() for the word "Liberty" in our data variable.

liberty = re.search(r'Liberty', data)