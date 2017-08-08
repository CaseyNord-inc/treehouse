import os
import random
import sys

# two variants of a function for clearing the console
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
