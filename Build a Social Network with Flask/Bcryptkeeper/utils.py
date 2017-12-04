# Import both generate_password_hash and check_password_hash from Flask-Bcrypt.

from flask.ext.bcrypt import generate_password_hash, check_password_hash

# Now create a function named set_password that takes a User and a string for their password.
# Hash the password, set the User.password attribute to the hashed password, and return the User.

def set_password(User, password):
    User.password = generate_password_hash(password)
    return User

# Finally write a function named validate_password that takes a user and a password.
# It should return True if the provided password, when hashed, matches the user's password. Otherwise, return False.

def validate_password(User, password):
    return check_password_hash(User.password, password)
