from actor import Actor
from cards import Cards
from house import House
from player import Player
from scoring import Scoring
from time import sleep
from random import shuffle

# Setting up our variables, arrays, and objects
card_list = []
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_score = [["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9], ["10", 10], ["Jack", 10], ["Queen", 10], ["King", 10], ["Ace", "Ace"], ]
round_number = 1
house = House()
player = Player()

# Creating our cards
for suit in suits:
    for rank in rank_score:
        card_list.append(Cards(suit, rank[0], rank[1]))

# Shuffling the deck
default_deck = card_list.copy()
shuffle(card_list)


# Dealing two cards for player and house (no relation to Dr. Gregory)
def opening_deal():
    house.opening_draw(card_list)
    player.opening_draw(card_list)

def player_win():
    return (player.final_score > house.final_score) and not (player.win or house.lost)


def house_win():
    return (player.final_score < house.final_score) and not (player.lost or house.win or house.lost)


def tie():
    return (player.final_score == house.final_score) and not (player.lost or house.lost or player.win or house.win)


def win_tracker(player, house):
    if player_win() or house.lost or player.win:
        player.total_wins += 1
    elif house_win() or player.lost or house.win:
        house.total_wins += 1


def gameplay(card_list, house, player):
    opening_deal()

    while player.hit_available:
        player.offer_hit(card_list)   

    if not (player.win or player.lost):
        house.house_behavior(player.final_score, card_list)

    if player_win():
        print(f"You win with a score of {player.final_score} to the house's {house.final_score}\n")
    elif house_win():
        print(f"House wins with a score of {house.final_score} to your {player.final_score}\n")        
    elif tie():
        print(f"You and the house are tied at {player.final_score} points each\n")


while True:
    for game in range(4):  # Plays 4 games before reshuffling
        house.reset()
        player.reset()
        print("=============================")
        print(f"\t    Round {round_number}")
        print(f"Player: {player.total_wins}     |     House: {house.total_wins}")
        print(f"\t    Ties: {round_number - 1 - (player.total_wins + house.total_wins)}")
        print("=============================")
        gameplay(card_list, house, player)
        sleep(2)
        win_tracker(player, house)
        round_number += 1
        
    card_list = default_deck.copy()
    shuffle(card_list)
