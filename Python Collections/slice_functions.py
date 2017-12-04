def first_4(iterable):
    return iterable[0:4]


def first_and_last_4(iterable):
    return iterable[:4] + iterable[-4::]


def odds(iterable):
    return iterable[1::2]


def reverse_evens(iterable):
    return iterable[::2][::-1]


test_list = [1, 2, 3, 4, 5]
new_list = reverse_evens(test_list)
print(new_list)
