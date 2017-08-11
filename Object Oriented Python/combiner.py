# Create a function named combiner that takes a single argument, which will be a list made up of strings and numbers.
# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers.
# For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2". Be sure to use isinstance to 
# solve this as I might try to trick you.

str_num_list = ["apple", 5.2, "dog", 8]

def combiner(str_num_list):
    str_list = []
    num_result = []
    for item in str_num_list:
        if isinstance(item, str) == True:
            str_list.append(item)
        if isinstance(item, (int, float)) == True:
            num_result.append(item)
        sums = sum(num_result)
    print(''.join(str_list) + str(sums))

combiner(str_num_list)