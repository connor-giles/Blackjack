"""This script holds the definition of the Chip class"""


class Chip:
    def __init__(self, total=100):
        self.total = total  # Allow user to choose starting chip amount or default to 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet  # If the user wins they get their bet back and they win their bet in profit

    def lose_bet(self):
        self.total -= self.bet  # If the user loses they lose their bet
