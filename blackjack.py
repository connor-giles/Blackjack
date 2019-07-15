"""
This is a program that imitates a simplified casino blackjack game
"""
import deck
import hand
import chips


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except TypeError:
            print('Please provide an integer')
        else:
            if chips.bet > chips.total:
                print('You do not have enough chips to make that bet!')
            else:
                break


def hit(d, h):
    single_card = d.deal()
    h.add_card(single_card)
    h.adjust_for_ace()


def hit_or_stand(d, h):
    global playing

    x = input("Would you like to hit or stand? Enter h or s")

    if x.lower() == 'h':
        hit(d, h)
    elif x.lower() == 's':
        print("Player stands, Dealer's turn")
        playing = False


def player_busts(player_hand, dealer_hand, chip):
    print('PLAYER BUSTS!')
    chip.lose_bet()


def player_wins(player_hand, dealer_hand, chip):
    print('PLAYER WINS!')
    chip.win_bet()


def dealer_busts(player_hand, dealer_hand, chip):
    print('PLAYER WINS! DEALER BUSTED!')
    chip.win_bet()


def dealer_wins(player_hand, dealer_hand, chip):
    print('DEALER WINS')
    chip.lose_bet()


def show_some_cards(player_hand, deal_hand):
    print("Dealer's Hand:")
    print("one card hidden!")
    print(deal_hand.cards[1])  # Shows the dealer's second card
    print('\n')

    print("Player's hand:")
    for c in player_hand.cards:
        print(c)
    print(player_hand.hand_value)
    print('\n')


def show_all_cards(player_hand, deal_hand):
    print("Dealer's Hand:")
    for c in deal_hand.cards:
        print(c)
    print(deal_hand.hand_value)

    print('\n')

    print("Player's hand:")
    for c in player_hand.cards:
        print(c)
    print(player_hand.hand_value)


def tie():
    print('Dealer and Player tie! PUSH')


playing = True  # A variable to determine if the game is being played

# GAME STARTS
#while True:
for i in range(1):
    game_deck = deck.Deck()     # The deck used for the game
    user_hand = hand.Hand()     # The user's hand throughout the turn
    dealer_hand = hand.Hand()   # The dealer's hand throughout the turn

    game_deck.shuffle()  # Ensures the deck is shuffled well

    user_hand.add_card(game_deck.deal())    # Gets the player's first card
    dealer_hand.add_card(game_deck.deal())  # Gets the dealer's first card
    user_hand.add_card(game_deck.deal())    # Gets the dealer's second card
    dealer_hand.add_card(game_deck.deal())  # Gets the player's second card

    user_chips = chips.Chip(1000)  # Player receives 1000 chips

    show_all_cards(user_hand, dealer_hand)
