def main():
    word = input("Enter a word to disemvowel: ")
    disemvowel(word)


def disemvowel(word):
    word_list = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in vowels:
        while True:
            try:
                word_list.remove(i)
            except ValueError:
                break
    print("{}".format(''.join(word_list)))


if __name__ == "__main__":
    main()
