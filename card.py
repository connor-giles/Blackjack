"""This script holds the definition of the Card class"""


class Card:

    # Sets up the Card object
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Overrides the str operator
    def __str__(self):
        return self.rank + ' of ' + self.suit
