import random
import time
import sys


def main():
    print("I want you to think of a number between 1 and 1000, and I'm going to guess it. I wonder how many tries it will take?\n")
    hidden_number = int(input("Enter a number: "))
    count = 1
    number_guess = random.randint(1, 1000)
    while True:
        if number_guess < hidden_number:
            print_slow("...")
            print("I guessed {}. Is that number is too low?".format(number_guess))
            count += 1
            number_guess = random.randint((number_guess + 1), hidden_number)
        elif number_guess > hidden_number:
            print_slow("...")
            print("I guessed {}. Is that number is too high?".format(number_guess))
            count += 1
            number_guess = random.randint(hidden_number, (number_guess - 1))
        else:
            print_slow("...")
            print("I guessed it! The number you were thinking of was {}! It took me {} tries to guess your number.".format(number_guess, count))
            break
    play_again()


def print_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)


def play_again():
    print("\nThat was fun! Can we play again? Y/n")
    yes_or_not = input().lower()

    if yes_or_not != 'n':
        main()
    else:
        print("Bye!")
        print_slow("...")


main()
