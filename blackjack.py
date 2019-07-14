"""
This is a program that imitates a simplified casino blackjack game
"""
import deck
import hand

# A variable to determine if the game is being played
playing = True

test_deck = deck.Deck()
test_deck.shuffle()

test_player = hand.Hand()

pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.hand_value)

pulled_card2 = test_deck.deal()
print(pulled_card2)
test_player.add_card(pulled_card2)
print(test_player.hand_value)


