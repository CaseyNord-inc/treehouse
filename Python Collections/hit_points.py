# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    if direction == (-1,0):
        x -= 1
        if x == 0:
            hp -= 5
            x += 1
    elif direction == (1,0):
        x += 1
        if x == 9:
            hp -= 5
            x -= 1
    elif direction == (0,-1):
        y -= 1
        if y == 0:
            hp -= 5
            y += 1
    elif direction == (0,1):
        y += 1
        if y == 9:
            hp -= 5
            y -=1
    return x, y, hp