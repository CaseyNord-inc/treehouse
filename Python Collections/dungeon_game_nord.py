# My version changes from Treehouse course project:
#   Added toggleable 'debug mode' to show everything on the map.
#   Upgraded input validation to show when inputs are invalid and not display 'hit wall' messages when unnecessary.
#   Added map to show locations of DOOR, MAP, KEY, and SWORD when found.
#   Added 'found door' feature that remembers location of door and informs player of KEY if KEY hasn't been found.
#   Added KEY that needs to be found before DOOR can be 'opened'.
#   Added SWORD item that gives you a chance to survive if the monster is encountered.
#   Gave monster the ability to move in a random direction once every other turn.

import random
import os

# wasd movement
# change player to a dictionary with a key that hold onto where the player has been.  Then when drawing map show every cell they've been in.


ROOMS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(ROOMS, 7)


def move_player(player, move):
    x, y = player
    if move in ["LEFT", "A"]:
        x -= 1
    if move in ["RIGHT", "D"]:
        x += 1
    if move in ["UP", "W"]:
        y -= 1
    if move in ["DOWN", "S"]:
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN", "W", "A", "S", "D"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
        moves.remove("A")
    if x == 4:
        moves.remove("RIGHT")
        moves.remove("D")
    if y == 0:
        moves.remove("UP")
        moves.remove("W")
    if y == 4:
        moves.remove("DOWN")
        moves.remove("S")
    return moves


def move_monster(monster, monster_move_choice, monster_turn):
    x, y = monster
    if monster_move_choice == "LEFT" and monster_turn == True:
        x -= 1
    if monster_move_choice == "RIGHT" and monster_turn == True:
        x += 1
    if monster_move_choice == "UP" and monster_turn == True:
        y -= 1
    if monster_move_choice == "DOWN" and monster_turn == True:
        y += 1
    return x, y


def get_monster_moves(monster, game_map, door, key, sword, secret_orb):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = monster
    mx, my = game_map
    dx, dy = door
    kx, ky = key
    sx, sy = sword
    ox, oy = secret_orb
    if x == 0 or (mx == x-1 and y == my) or (dx == x-1 and y == dy) or (kx == x-1 and y == ky) or (sx == x-1 and y == sy) or (ox == x-1 and y == oy):
        moves.remove("LEFT")
    if x == 4 or (mx == x+1 and y == my) or (dx == x+1 and y == dy) or (kx == x+1 and y == ky) or (sx == x+1 and y == sy) or (ox == x+1 and y == oy):
        moves.remove("RIGHT")
    if y == 0 or (my == y-1 and x == mx) or (dy == y-1 and x == dx) or (ky == y-1 and x == kx) or (sy == y-1 and x == sx) or (oy == y-1 and x == ox):
        moves.remove("UP")
    if y == 4 or (my == y+1 and x == mx) or (dy == y+1 and x == dx) or (ky == y+1 and x == kx) or (sy == y+1 and x == sx) or (oy == y+1 and x == ox):
        moves.remove("DOWN")
    return moves


def draw_map(found_map, found_door, has_key, has_sword, has_secret_orb, debug, player, monster, game_map, door, key, sword, secret_orb):
    print(" _"*5)
    tile = "|{}"

    for cell in ROOMS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == door and (debug == True or found_map == True or found_door == True):
                output = tile.format("D")
            elif cell == key and (debug == True or found_map ==True or has_key == True):
                output = tile.format("K")
            elif cell == sword and (debug == True or found_map ==True or has_sword == True):
                output = tile.format("S")
            elif cell == secret_orb and (debug == True or has_secret_orb == True):
                output = tile.format("T")
            elif cell == monster and (debug == True or has_secret_orb == True):
                output = tile.format("O")
            elif cell == game_map and (debug == True or found_map == True):
                output = tile.format("M")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == door and (debug == True or found_map == True or found_door == True):
                output = tile.format("D|")
            elif cell == key and (debug == True or found_map ==True or has_key == True):
                output = tile.format("K|")
            elif cell == sword and (debug == True or found_map ==True or has_sword == True):
                output = tile.format("S|")
            elif cell == secret_orb and (debug == True or has_secret_orb == True):
                output = tile.format("T|")
            elif cell == monster and (debug == True or has_secret_orb == True):
                output = tile.format("O|")
            elif cell == game_map and (debug == True or found_map == True):
                output = tile.format("M|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    player, monster, game_map, door, key, sword, secret_orb = get_locations()
    playing = True
    monster_turn = True
    found_map = False
    found_door = False
    has_key = False
    has_sword = False
    has_secret_orb = False
    debug = False
    valid_inputs = ["LEFT", "RIGHT", "UP", "DOWN", "W", "A", "S", "D", "QUIT", "DEBUG"]
    wall_checks = ["QUIT", "DEBUG"]


    while playing:
        clear_screen()
        draw_map(found_map, found_door, has_key, has_sword, has_secret_orb, debug, player, monster, game_map, door, key, sword, secret_orb)
        valid_moves = get_moves(player)
        valid_monster_moves = get_monster_moves(monster, game_map, door, key, sword, secret_orb)

        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** See you next time! ** \n")
            break
        if move == 'DEBUG':
            if debug == False:
                debug = True
            elif debug == True:
                debug = False
        if move not in valid_inputs:
            input("\n ** That is not a valid input! **\n")
        elif move in valid_moves:
            if monster_turn == True:
                monster_move_choice = random.choice(valid_monster_moves)
                monster = move_monster(monster, monster_move_choice, monster_turn)
                monster_turn = False
            elif monster_turn == False:
                monster_turn = True
            player = move_player(player, move)
            if player == game_map:
                if found_map == False:
                    found_map = True
                    input("\n ** You've found a map of the dungeon that reveals the location of the KEY and the EXIT! Something else is on here too, it might be worth investigating! **\n")
                elif found_map == True:
                    continue
            if player == key:
                if has_key == False:
                    has_key = True
                    input("\n  ** You've found a key! You might need this to open a door... **\n")
                if has_key == True:
                    continue
            if player == door:
                if has_key == False:
                    found_door = True
                    input("\n ** You've found the door but it is locked and won't budge. There must be key hidden somewhere else in the dungeon! **\n")
                elif has_key == True:
                    input("\n ** You try the key to open the door and it works! You've escaped the dungeon! Congratulations! ** \n")
                    playing = False
            if player == sword:
                if has_sword == False:
                    has_sword = True
                    input("\n  ** You've found a sword! It appears old and brittle but might help you defend against any dangers! **\n")
                if has_sword == True:
                    continue
            if player == secret_orb:
                if has_secret_orb == False:
                    has_secret_orb = True
                    input("\n  ** You've found a secret orb! Peering into it reveals the location of the dungeon's monster. This should help you survive! **\n")
                if has_secret_orb == True:
                    continue
            if player == monster:
                if has_sword == True:
                    has_sword = False
                    input("\n ** You encounter the monster of the dungeon! You fight for your life and just barely manage to escape. Your brittle sword is destroyed in the fray, better be careful! **\n")
                elif has_sword == False:
                    print("\n ** Oh no, the monster got you! With nothing to defend yourself you didn't stand a chance, better luck next time! ** \n")
                    playing = False
        elif move not in wall_checks:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()


#Welcome the user and initialize game
clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
   