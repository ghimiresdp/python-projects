import random

SCREEN_SIZE = 80
TITLE = """
██    ██   ██████   ███   ██   ██████   ██    ██   ██████   ███   ██
██    ██  ██    ██  ████  ██  ██        ███  ███  ██    ██  ████  ██
████████  ████████  ██ ██ ██  ██  ████  ██ ██ ██  ████████  ██ ██ ██
██    ██  ██    ██  ██  ████  ██    ██  ██    ██  ██    ██  ██  ████
██    ██  ██    ██  ██   ███   ███████  ██    ██  ██    ██  ██   ███
"""

LOOSER = """
██         ██████    ██████    ███████  ████████  ███████
██        ██    ██  ██    ██  ██        ██        ██    ██
██        ██    ██  ██    ██   ██████   ████████  ████████
██        ██    ██  ██    ██        ██  ██        ██  ██
████████   ██████    ██████   ███████   ████████  ██   ███
"""

WINNER = """
██    ██  ████████  ███   ██  ███   ██  ████████  ███████
██    ██     ██     ████  ██  ████  ██  ██        ██    ██
██ ██ ██     ██     ██ ██ ██  ██ ██ ██  ████████  ███████
███  ███     ██     ██  ████  ██  ████  ██        ██  ██
██    ██  ████████  ██   ███  ██   ███  ████████  ██   ███
"""

greetings = [
    "We are so excited to have you on our team, {}!",
    "We are thrilled to have you at our terminal, {}!",
    "Welcome {}!! lets start the exciting game",
]

questions = [
    {
        "word": "computer",
        "definition": "An electronic device that is used for storing, and computing data in digital form.",
    },
    {
        "word": "programming",
        "definition": "The process of instructing the computer todo certain task.",
    },
    {
        "word": "inheritance",
        "definition": "The process by which a child class takes a base from an another class to retain similar implementation",
    },
    {
        "word": "polymorphism",
        "definition": "The ability of a program in OOP that is able to show different characteristics in different situations",
    },
    {
        "word": "dictionary",
        "definition": "A data type in python that has key-value pair",
    },
    {
        "word": "comprehension",
        "definition": "A method of generating different collection data types based on another collection of data",
    },
    {
        "word": "lambda",
        "definition": "An anonymous function that is used as one liner function",
    },
    {
        "word": "iteration",
        "definition": "The method of running a sequence of instructions or code in a repeated manner "
                      "until specific result is achieved",
    },
]


def display_line():
    print("=" * SCREEN_SIZE)


class Question:
    def __init__(self, word: str, definition) -> None:
        self.__word = word.upper()
        self.definition = definition
        self.remaining = 5
        self.__correct = 0
        self.__attempts = 0
        self.__progress = ["__" for char in word]

    def check_answer(self, guess: str):
        # todo: add the logic here
        guess = guess.upper()
        self.__attempts += 1
        for character in guess:
            if self.remaining > 0:
                if character in self.__word:
                    for index, ch in enumerate(self.__word):
                        if ch == character and self.__progress[index] == '__':
                            self.__progress[index] = character
                            self.__correct += 1
                else:
                    self.remaining -= 1
        if "__" in self.__progress:
            return False
        return True

    def render(self):
        print(self.definition, end="\n\n")
        print("Total Attempts:", self.__attempts)
        print("Total Correct Guesses:", self.__correct)
        print("Remaining Lives:", self.remaining)

        print("+", "-" * SCREEN_SIZE, "+", sep="")
        print("|", " " * SCREEN_SIZE, "|", sep="")

        # print("|", "I N H E R I T A N C E".center(SCREEN_SIZE), "|", sep="")
        print("|", ("  ".join(self.__progress)).center(SCREEN_SIZE), "|", sep="")

        print("|", " " * SCREEN_SIZE, "|", sep="")
        print("+", "-" * SCREEN_SIZE, "+", sep="")


class Hangman:
    def __init__(self, player):
        self.player = player
        self.options = ["", ""]
        self.question = None

        print(greetings[random.randint(0, len(greetings) - 1)].format(self.player))
        display_line()

        print("Lets start with the word:\n")

    def shuffle(self):
        current = questions[random.randint(0, len(questions) - 1)]
        # return Question(current['word'], current['definition'])
        self.question = Question(**current)

    def play(self):
        self.shuffle()
        while self.question.remaining > 0:
            self.question.render()
            guess = input("Enter your guess: ")
            completed = self.question.check_answer(guess)
            if completed:
                self.question.render()
                print(WINNER)
                break
        else:
            print(LOOSER)


if __name__ == '__main__':
    print(TITLE)
    display_line()
    player = input('Please Enter your name: ')
    hangman = Hangman(player)
    hangman.play()
