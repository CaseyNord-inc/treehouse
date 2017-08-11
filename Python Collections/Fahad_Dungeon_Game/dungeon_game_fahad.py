import random
import sys


CELLS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
         (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
         (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
         (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
         (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
         (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)] 
from monster import Monster

jubjub = Monster(name='Jubjub', damage=2, sound='tweet!')
poo = Monster(name='Honey The Poo', damage=0, sound='poop...')
goliath = Monster(name='The Goliath', damage=3, sound='roar!')
anaconda = Monster(name='The Anaconda', damage=1, sound='SsSSsS', attack='bitten')

monsters = [jubjub, poo, goliath, anaconda]

monster = random.choice(monsters)
monsters.remove(monster)
monster2 = random.choice(monsters)

def exit():
    sys.exit()

def get_locations():

    monster_position = random.choice(CELLS)

    door = random.choice(CELLS)

    start = random.choice(CELLS)
    monster2_position = random.choice(CELLS)
    mine_locations = random.sample(CELLS, 8)


    if monster_position == start or monster_position == door or monster2_position == start or monster2_position == door or start == door:
        return get_locations()
    if monster_position in mine_locations or start in mine_locations or door in mine_locations or monster2_position in mine_locations:
        return get_locations()


    return monster_position, door, start, monster2_position, mine_locations

def move_monster_closer(player):

    px, py = player

    x1, y1 = px - 1, py - 1
    x2, y2 = px - 1, py
    x3, y3 = px - 1, py + 1
    x4, y4 = px, py - 1
    x5, y5 = px, py + 1
    x6, y6 = px + 1, py - 1
    x7, y7 = px + 1, py
    x8, y8 = px + 1, py + 1

    xy_list = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8)]
    bad_locations = []

    for xy_item in xy_list:
        if xy_item[0] > 5 or xy_item[1] > 5 or xy_item[0] < 0 or xy_item[1] < 0:
            bad_locations.append(xy_item)
    for xy_item in bad_locations:
        while True:
            try:
                xy_list.remove(xy_item)
            except:
                break


    monster_position = random.choice(xy_list)
    xy_list.remove(monster_position)

    monster2_position = random.choice(xy_list)
    return monster_position, monster2_position






def move_player(player, move):


    x, y = player

    if move == 'LEFT':
        y-=1
    elif move == 'RIGHT':
        y+=1
    elif move == 'UP':
        x-=1
    elif move == 'DOWN':
        x+=1
    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    #player = (x, y)
    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 5:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 5:
        moves.remove('DOWN')

    return moves

def draw_map(player, monster_position, monster2_position, door, mine_locations):

    print(' _ _ _ _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):

        if idx in [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28,
                 30, 31, 32, 33, 34]:
            if cell == player:
                print(tile.format('X'), end='')
            elif cell == monster_position:
                print(tile.format('@'), end='')
            elif cell in mine_locations:
                print(tile.format('#'), end='')
            elif cell == door:
                print(tile.format('D'), end='')
            else:
                print(tile.format('_'), end='')
        else:

            if cell == player:
                print(tile.format('X|'))
            elif cell == monster_position:
                print(tile.format('@|'))
            elif cell in mine_locations:
                print(tile.format('#|'))
            elif cell == door:
                print(tile.format('D|'))
            else:
                print(tile.format('_|'))

def display_info(player, monster_position, monster2_position, door, mine_locations, health, moves):

    print("You're currently in room {}".format(player))
    print("You are being hunted by {} and {} hiding in the shadows".format(monster.name, monster2.name))
    print("{} has {} hit point(s) so watch out!".format(monster.name, monster.damage))

    draw_map(player, monster_position, monster2_position, door, mine_locations)
    print("Hidden monster location: {}".format("Unknown"))
    print("Health status: {}".format(health))
    print("You can move {}".format(moves))
def display_update_message(message):
    print("UPDATE MESSAGE: {}".format(message.upper()))
def run_game(monster, monster2):
    print("Welcome to the dungeon!")
    print("Your objective is to reach the door marked as 'D' on the map. You are 'X'")
    print("RULES: ")
    print(">The hidden monster is always a 1 hit kill")
    print(">Your maximum health is 3")
    print(">Each monster does a different amount of damage. Some can kill you in 1 attack")
    print(">Dont step on the mines!")
    print("Enjoy! :D ")
    health = 2
    monster_position, door, player, monster2_position, mine_locations = get_locations()
    while True:
        print("------------------------------------------------")
        moves = get_moves(player)
        display_info(player, monster_position, monster2_position, door, mine_locations, health, moves)

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            break
        if move in moves:
            player = move_player(player, move)
        else:
            print("**Walls are hard. Stop walking into them! **")
            continue

        if player == monster_position:
            health-=monster.damage
            if health > 0:
                display_update_message("You were almost eaten! though the extent of your injuries give you a chance of survival;\nDo not expect to be so lucky next time!")

        if health == 0 and player == monster_position:
            print("Ouch! You were eaten by the monster!")
            print("{} says: {}!!!".format(monster.name, monster.battlecry()))
            exit()   
        elif player == door:
            print("You escaped!")
            exit()
        elif player == monster2_position:
            print("Ouch! You were eaten by the second hidden monster!")
            exit()
        elif player in mine_locations:
            print("*BOOM!* You hit a mine! x_x ")
            exit()
        #print("Monster 2 is currently in room {}".format(monster2))
        monster_position, monster2_position = move_monster_closer(player)

run_game(monster, monster2)    