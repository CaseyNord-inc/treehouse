# Hannah's DungeonGame v1.0
# Copyright (c) 2014 Hannah Taylor

import random

rooms = []
MESSAGES = ['So far so good, still alive, but no door here',
            'Hmm, nothing here, keep moving.',
            'WAIT! What was that sound?  Oh, nothing, not a monster and no door in sight',
            'Warmer... Or maybe colder.',
            'Hurry hurry!',
            "Are you sure you know where you're going?"]

def create_map(width, height):
    global rooms

    for y in range(height):
        for x in range(width):
            rooms.append((x, y))

def create_room():
    global player, door, monster, breadcrumbs

    #Put the player in a spot
    player = random.choice(rooms)
    breadcrumbs.append(player)

    #Put the door in a different spot to player
    valid = False
    while valid == False:
        door = random.choice(rooms)
        if door != player:
            valid = True

    #Put the monster in a different spot to player and door
    valid = False
    while valid == False:
        monster = random.choice(rooms)
        if monster != player and monster != door:
            valid = True
    #Uncomment to debug
    #print('player: {}, door: {}, monster: {}'.format(player, door, monster))

def draw_map(mode):
    global player, breadcrumbs, rooms, width, height

    for y in range(height):
        print("","------" * width + "-")
        for x in range(width):
            print(" | ",end="")
            curr_position = breadcrumbs[len(breadcrumbs)-1]
            if (x, y) == curr_position:
                if mode == "door":
                    print(" \u26BF ",end="")
                elif mode == "monster":
                    print(" \u2620 ",end="")
                else:
                    print(" \u263A ",end="")
            elif (x, y) in breadcrumbs:
                print(" * ",end="")
            else:
                print("   ",end="")
        print(" |")
    print("","------" * width + "-")
    #print(rooms)

def move(direction):
    global player, breadcrumbs, width, height

    if direction in ['left','a']:
        if player[0] > 0:
            coords = rooms.index(player)
            new_coords = rooms[coords-1] 
        else:
            return None
    elif direction in ['right','d']:
        if player[0] < width-1:
            coords = rooms.index(player)
            new_coords = rooms[coords+1]
        else:
            return None

    elif direction in ['up','w']:
        if player[1] > 0:
            coords = rooms.index(player)
            new_coords = rooms[coords-width]
        else:
            return None

    elif direction in ['s','down']:
        if player[1] < height-1:
            coords = rooms.index(player)
            new_coords = rooms[coords+width]
        else:
            return None

    breadcrumbs.append(new_coords)
    return new_coords


def check_position():
    global player, door, monster

    if player == door:
        print("\n\nYou found the door! you win!")
        moving = "door"
    elif player == monster:
        print("\n\nYou got eaten by the monster, you lose!")
        moving = "monster"
    else:
        print("\n\n"+random.choice(MESSAGES)) #make a list of messages and use random.choice()
        moving = True

    return moving

def play_again(repeat):
    playagain = input("Would you like to play again? Y/N")
    if playagain in ["n","no"]:
        repeat = False

    return repeat

# Game Loop
repeat = True
while repeat == True:
    #Welcome the user
    print("Welcome to the dungeon!")
    print("Choose your challenge by setting the room size: \n\n")

    #Set room size
    width, height = "", ""
    while not width.isnumeric():
        width = input("Enter room width: ")

    while not height.isnumeric():
        height = input("Enter room height: ")

    width, height = int(width), int(height)

    #Initialise variables
    breadcrumbs = []

    player = ""
    door = ""
    monster = ""

    #Set up game
    create_map(width, height)
    create_room()

    #Instructions
    print("\n\nThere is a monster lurking in the depths of this dungeon, and only one way to escape")
    print("Find the door before you are eaten by the monster!")
    print("\n\nThis handy map will show you where you have been")

    draw_map(True)

    print("\nWhenever you see > you can choose to move left, right up or down with those words or the WASD keys, followed by enter")

    moving = True
    while moving == True:
        direction = input("> ")
        if direction in ['left','right','up','down','w','a','s','d']:
            position = move(direction)
            if position == None:
                print("\nAh, there are no more rooms that way, you're at the edge of the map!")
            else:
                player = position
                moving = check_position()
                draw_map(moving)

                #Uncomment to debug
                #print('DEBUG: player: {}, door: {}, monster: {}'.format(player, door, monster))
        else:
            print("Please choose left right up down or w a s d")

    repeat = play_again(repeat)

print("Thanks for playing!")