import os

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def add_to_list(new_item):
    show_help()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, new_item)
    else:
        shopping_list.append(new_item)

    show_list()


def show_list():
    clear_screen()

    print("Here's your list:\n")

    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))

    print("-"*10)


def move_item():
    show_list()
    what_to_move = input("What would you like to move?\n")
    try:
        move_index = shopping_list.index(what_to_move)
        pop_holder = shopping_list.pop(move_index)
        where_to_move = input("What position would you like this to be in your list?\n")
        try:
            move_parse = int(where_to_move) - 1
            shopping_list.insert(move_parse, pop_holder)
        except TypeError:
            print("That is not a valid location.")
    except ValueError:
        print("Your list does not contain {}.".format(what_to_move))
    input("Press ENTER to continue.\n")
    show_list()


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


def clear_list():
    del shopping_list[:]
    show_list()


def save_list():
    file = open('shopping_list_2.txt', 'w')

    for item in shopping_list:
        file.write(item + '\n')

    file.close()
    show_list()


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to show the items currently on the list.
Enter 'MOVE' to move an item in this list.
Enter 'REMOVE' to delete an item from your list.
Enter 'CLEAR' to clear all the items from your list.
Enter 'HELP' to show a list of useful commands.
Enter 'SAVE' to save the list to as .txt
""")


def main():
    show_help()

    while True:
        new_item = input("> ")

        if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
            break
        elif new_item.upper() == 'SHOW':
            show_list()
            continue
        elif new_item.upper() == 'HELP':
            show_help()
            continue
        elif new_item.upper() == 'SAVE':
            save_list()
            continue
        elif new_item.upper() == 'REMOVE':
            remove_from_list()
            continue
        elif new_item.upper() == 'CLEAR':
            clear_list()
            continue
        elif new_item.upper() == 'MOVE':
            move_item()
            continue
        else:
            add_to_list(new_item)

    show_list()


main()
