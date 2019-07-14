"""This script holds the definition of the Hand class"""
import card
import deck


class Hand:
    def __init__(self):
        self.cards = []  # A list of the current cards in the user's hand
        self.hand_value = 0  # The actual value of the user's hand
        self.num_aces = 0  # Keeps track of the number of aces that the user has

    def __len__(self):
        return len(self.cards)

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.hand_value += deck.values[new_card.rank]

        if new_card.rank == 'Ace':
            self.num_aces += 1

    def adjust_for_ace(self):
        # If the users hand value is greater than 21 but the user still has an ace, you need to re-adjust the hand value
        while self.hand_value > 21 and self.num_aces:
            self.hand_value -= 10
            self.num_aces -= 1
