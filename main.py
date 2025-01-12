import config
from word import Word
from api import API


def main():
    word = Word()

    print("### Welcome to Wordle Game ###")
    for attempt in range(1, config.attempts + 1):
        picked_word = word.pick()

        print(f"Attempt {attempt} --> Picked Word: {picked_word}")
        feedback = API.daily(picked_word)

        if word.guessed(feedback):
            print(f"Congrats! You have guessed the word.\nGuessed word: {picked_word}")
            return

        word.train(feedback)

    print("You failed to guess the word. Better luck next time.")


if __name__ == "__main__":
    main()
