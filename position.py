import config
import random
import copy


class Position:
    def __init__(self):
        self.possible_letters = copy.deepcopy(config.possible_letters)

    def pick(self):
        return random.choice(list(self.possible_letters))
