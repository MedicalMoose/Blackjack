from actor import Actor
from cards import Cards
from house import House
from player import Player
from scoring import Scoring
from random import shuffle

# Setting up our variables, arrays, and objects
card_list = []
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_score = [["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9], ["10", 10], ["Jack", 10], ["Queen", 10], ["King", 10], ["Ace", "Ace"], ]
house = House()
player = Player()

# Creating our cards
for suit in suits:
    for rank in rank_score:
        card_list.append(Cards(suit, rank[0], rank[1]))

# Shuffling the deck
shuffle(card_list)


# Dealing two cards for player and house (no relation to Dr. Gregory)
def opening_deal():
    house.opening_draw(card_list)
    player.opening_draw(card_list)

opening_deal()

while player.hit_available:
    player.offer_hit(card_list)   

if not (player.win or player.lost):
    house.house_behavior(player.final_score, card_list)

if player.final_score > house.final_score or player.win or house.lost:
    print(f"You win with a score of {player.final_score} to the house's {house.final_score}")
elif player.final_score < house.final_score or house.win:
    print(f"House wins with a score of {house.final_score} to your {player.final_score}")        
else:
    print(f"You and the house are tied at {player.final_score} points each")