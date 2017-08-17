# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

iter1 = [1, 2, 3]
iter2 = 'abc'


def combo(iter1, iter2):
    list_of_tuples = []
    for index, item in enumerate(iter2):
        list_of_tuples.append((iter1[index], item))
    print(list_of_tuples)


combo(iter1, iter2)
