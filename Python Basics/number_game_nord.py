import random
import time
import sys

# generate a random number between 1 and 10
hidden_number = random.randint(1, 10)


def main():
    count = 1
    # compare guess to secret number
    # print hit/miss
    while True:
        try:
            number_guess = int(input("Enter a number: "))
        except ValueError:
            print("That is not a valid input, please try again.")
        else:
            if number_guess < hidden_number:
                print("That number is too low, try again!")
                count += 1
            elif number_guess > hidden_number:
                print("That number is too high, try again!")
                count += 1
            else:
                print("You guessed it! The number I was thinking of was {}! It took you {} tries to guess my number.".format(number_guess, count))
                break
    play_again()


def print_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)


def play_again():
    print("\nThat was fun! Would you like to play again? Y/n")
    yes_or_not = input().lower()

    if yes_or_not != 'n':
        main()
    else:
        print("Bye!")
        print_slow("...")


# get a number guess from the player
print("I am thinking of a number between 1 and 10. Can you guess the number?\n")
main()
