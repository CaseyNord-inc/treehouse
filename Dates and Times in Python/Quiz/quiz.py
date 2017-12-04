import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        # Generate 10 random questions with numbers from 1 to 10
        for _ in range(10):
            # Add these questions into self.questions
            self.questions.append(random.choice(question_types)(random.randint(1, 10), random.randint(1, 10)))

    def take_quiz(self):
        # Log the start time
        self.start_time = datetime.datetime.now()
        # Ask all of the questions
        for question in self.questions:
            # Log if they got the question right
            self.answers.append(self.ask(question))
        else:
            # Log the end time
            self.end_time = datetime.datetime.now()
        # Show a summary
        return self.summary()

    def ask(self, question):
        correct = False
        # Log the start time
        question_start = datetime.datetime.now()
        # Capture the answer
        answer = input(question.text + ' = ')
        # Check the answer
        if answer == str(question.answer):
            correct = True
        # Log the end time
        question_end = datetime.datetime.now()
        # If the answer is right, send back true
        # Otherwise, send back false
        # Send back the elapsed time, too
        return correct, question_end - question_start

    def total_correct(self):
        # return the total number of correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # Print how many you got right and the total # of questions. 5/10
        print("You got {} out of {} right.".format(
                self.total_correct(), len(self.questions)
        ))
        # Print the total time for the quiz: 30 seconds!
        print("It took you {} seconds total.".format(
                (self.end_time-self.start_time).seconds
        ))


Quiz().take_quiz()
