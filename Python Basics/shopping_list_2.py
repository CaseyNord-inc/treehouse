# make a list to hold onto our items
shopping_list = []


def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))


def show_list():
    # print out the list
    print("Here's your list:\n")

    for item in shopping_list:
        print(item)


def save_list():
    file = open('shopping_list_2.txt', 'w')

    for item in shopping_list:
        file.write(item + '\n')

    file.close()


def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to show the items currently on the list.
Enter 'HELP' to show a list of useful commands.
Enter 'SAVE' to save the list to as .txt
""")


def main():
    show_help()

    # ask for new items
    while True:
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'SHOW':
            show_list()
            continue
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SAVE':
            save_list()
            continue
        add_to_list(new_item)

    show_list()


main()
