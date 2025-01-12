import config
from position import Position
from constant import LetterStatus


class Word:

    def __init__(self):
        self.length = config.word_length
        self.positions = []
        for _ in range(self.length):
            self.positions.append(Position())
        self.picked_words = []

    def pick(self):
        word = []
        for position in self.positions:
            letter = position.pick()
            word.append(letter)

        self.picked_words.append("".join(word))

        return self.picked_words[-1]

    def train(self, feedback):
        for letter_info in feedback:
            slot = letter_info["slot"]
            letter = letter_info["guess"]
            status = letter_info["result"]

            if status == LetterStatus.CURRECT:
                self.positions[slot].possible_letters = set(letter)
            elif status == LetterStatus.ABSENT:
                for position in self.positions:
                    position.possible_letters.discard(letter)
            elif status == LetterStatus.PRESENT:
                self.positions[slot].possible_letters.discard(letter)

    def guessed(self, feedback):
        word_guessed = True
        for letter_info in feedback:
            status = letter_info["result"]
            if status != LetterStatus.CURRECT:
                word_guessed = False
                break

        return word_guessed
