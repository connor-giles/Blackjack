"""This script holds the definition of the Deck class"""
import random
import card

# A tuple to hold the 4 kinds of suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# A tuple to hold the ranks of the cards
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# A dictionary that pair ranks with blackjack values
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Deck:

    def __init__(self):
        self.deck = []  # List to hold the deck info
        for suit in suits:  # Loops through all suits and ranks to "make the deck"
            for rank in ranks:
                single_card = card.Card(suit, rank)
                self.deck.append(single_card)

    def __str__(self):
        deck_composition = ''
        for c in self.deck:
            deck_composition += '\n' + c.__str__()
        return 'The deck is composed of: ' + deck_composition

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card



