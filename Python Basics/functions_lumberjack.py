def hows_the_parrot():
    print("He's pining for the fjords!")


hows_the_parrot()


def lumberjack(name):
    if name.lower() == 'casey':
        print("Casey's a lumberjack and he's OK!")
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))


lumberjack("Casey")


def lumberjack2(name, pronoun):
        print("{}'s a lumberjack and {}'s OK!".format(name, pronoun))
        print("{} sleeps all night and {} works all day!".format(pronoun, pronoun))


lumberjack2("Casey", "he")
lumberjack2("Kira", "she")
