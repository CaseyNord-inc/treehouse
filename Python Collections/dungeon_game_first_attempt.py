import random

    # draw grid
    # pick random location for player
    # pick random location for exit door
    # pick random location for monster
    # draw player in the grid
    # take input for movement
    # move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def get_locations():
    locations = random.sample(CELLS, 3)
    monster = locations[0]
    door = locations[1]
    player = locations[2]

    return monster, door, player


def move_player(player, move):
    # get the player's location
    player_location = player
    # if move == LEFT, x-1
    if move == "LEFT":
        x, y = player_location
        player = x-1, y
    # if move == RIGHT, x+1
    if move == "RIGHT":
        x, y = player_location
        player = x+1, y
    # if move == UP, y-1
    if move == "UP":
        x, y = player_location
        player = x, y-1
    # if move == DOWN, y+1
    if move == "LEFT":
        x, y = player_location
        player = x, y+1
    return player

def get_moves(player):
    x_pos, y_pos = player
    # if player's y == 0, they can't move up
    if y_pos == 0 and move == "UP":
        print("You can't move any further in that direction!")
    # if player's y == 4, they can't move down
    elif y_pos == 4 and move == "DOWN":
        print("You can't move any further in that direction!")
    # if player's x == 0, they can't move left
    elif x_pos == 0 and move == "LEFT":
        print("You can't move any further in that direction!")
    # if player's x == 4, they can't move right
    elif x_pos == 4 and move == "RIGHT":
        print("You can't move any further in that direction!")
    else:
        move_player(player, move)
    return move

def available_moves(player):
    x_pos, y_pos = player
    list_of_moves = []
    if y_pos != 0:
        list_of_moves.append("UP")
    elif y_pos != 4:
        list_of_moves.append("DOWN")
    elif x_pos != 0:
        list_of_moves.append("LEFT")
    elif x_pos != 4:
        list_of_moves.append("RIGHT")
    return list_of_moves

def win_loss(player, door, monster):
    if player == door:
        print("You win!")
    elif player == monster:
        print("You lose!")


while True:
    print("Welcome to the dungeon!")
    print("You're currently in room {}".format(player)) # fill with player position
    print("You can move {}") # fill with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    # Good move? Change the player position
    # Bad move? Don't change anything!
    # On the door? They win!
    # On the door? They lose!
    # Otherwise, loop back around