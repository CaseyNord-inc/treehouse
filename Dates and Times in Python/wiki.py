import datetime


answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

answer_list = []

while True:
    answer = input("What dates would you like? Please use the MM/DD format. Enter 'done' to create links. Enter 'quit' to quit.\n")
    if answer.upper() == 'QUIT':
        break
    try:
        if answer.upper() == 'DONE':
            for answer in answer_list:
                date = datetime.datetime.strptime(answer, answer_format)
                output = link.format(date.strftime(link_format))
                print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")
    answer_list.append(answer)
