import config
import random


class Position:
    def __init__(self):
        self.possible_letters = config.possible_letters

    def pick(self):
        return random.choice(list(self.possible_letters))
