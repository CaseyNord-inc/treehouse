sample_string = "I do not like it Sam I Am"
def word_count(sample_string):
    sample_string = sample_string.lower()
    string_list = sample_string.split()
    word_dict = {}
    for cur_string in string_list:
        count = 0
        for string in string_list:
            if cur_string == string:
                count +=1
        word_dict[cur_string] = count
    print(word_dict)

word_count(sample_string)