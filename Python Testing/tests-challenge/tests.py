# Import the unittest module.

import unittest

# Create a TestCase named SimpleTestCase with a simple test
# that asserts that 10 - 10 is 0. Remember, unittest test names have to start with test_.

class SimpleTestCase(unittest.TestCase):
    def test_ten_minus_ten(self):
        assert 10 - 10 == 0

# We haven't used assertTrue yet but I'm sure you can handle this.
# assertTrue checks that a value is truthy. Complete the first test using assertTrue.
# Provide your own good palindrome or use "tacocat".

from string_fun import is_palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        self.assertTrue(is_palindrome(self.tacocat))


# Great! Now let's use the reverse of assertTrue which is assertFalse.
# Fill out test_bad_palindrome with the assertFalse assertion and a bad palindrome.

    def test_bad_palindrome(self):
        self.assertFalse(is_palindrome(self.catbird))

# The get_anagrams() function takes one or more words and returns anagrams for each of them as a list.
# Finish the test_in_anagrams() test to check that the anagrams for the string "treehouse" contains the word "house".

from string_fun import get_anagrams


class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        self.assertIn("house", get_anagrams("Treehouse"))

# Conversely, we shouldn't see the word "code" in the list of anagrams for "treehouse".
# Add a new test named test_not_in_anagrams and use self.assertNotIn() to make sure "code" isn't in the anagrams for "treehouse".

    def test_not_in_anagrams(self):
        self.assertNotIn("code", get_anagrams("Treehouse"))

    # Our get_anagrams() function raises a ValueError when you pass it an empty string.
    # Finish the test to make sure this happens. You'll want to use assertRaises.

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams('')

# Now add a new test, test_no_args that should also assertRaises(ValueError).
# This time, call get_anagrams() with no arguments.

    def test_no_args(self):
        with self.assertRaises(ValueError):
            get_anagrams()