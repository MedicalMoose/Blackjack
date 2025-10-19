from cards import Cards
from scoring import Scoring
from random import shuffle

# Setting up our variables, arrays, and objects
card_list = []
played_cards = []
player_hand = []
house_hand = []
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_score = [["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9], ["10", 10], ["Jack", 10], ["Queen", 10], ["King", 10], ["Ace", "Ace"], ]
player_score = Scoring([])
house_score = Scoring([])

# Creating our cards
for suit in suits:
    for rank in rank_score:
        card_list.append(Cards(suit, rank[0], rank[1]))

# Shuffling the deck
shuffle(card_list)

# Dealing two cards for player and house (no relation to Dr. Gregory)
def opening_deal():
    for cards in range(2):
        player_hand.append(card_list.pop())
        house_hand.append(card_list.pop())

    print(f"House:\t{house_hand[0]}, ???")
    print(f"Player:\t{player_hand[0]}, {player_hand[1]}")
    print("Hit (h) or Stand (s)?")

# Draws another card for the player, checks if they busted
def hit():
    player_hand.append(card_list.pop())
    for card in player_hand:
        print(card)
    if player_score.get_score() > 21:

def stand():

    

opening_deal()
hit()