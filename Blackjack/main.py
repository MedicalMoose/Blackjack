from cards import Cards
from house import House
from player import Player
from time import sleep
from random import shuffle

# Setting up our variables, arrays, and objects
card_list = []
played_cards = []
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
    house.opening_draw(card_list, played_cards)
    player.opening_draw(card_list, played_cards)

def player_win():
    return (player.final_score > house.final_score) and not (player.win or house.lost)


def house_win():
    return (player.final_score < house.final_score) and not (player.lost or house.win or house.lost)


def tie():
    return (player.final_score == house.final_score) and not (player.lost or house.lost or player.win or house.win)


def win_tracker(user_player, house_player):
    if player_win() or house_player.lost or user_player.win:
        user_player.total_wins += 1
    elif house_win() or user_player.lost or house_player.win:
        house_player.total_wins += 1


def gameplay(cards, house_player, user_player, played):
    opening_deal()

    while user_player.hit_available:
        user_player.offer_hit(cards, played)

    if not (user_player.win or user_player.lost):
        house_player.house_behavior(user_player.final_score, cards)

    if player_win():
        print(f"You win with a score of {user_player.final_score} to the house's {house_player.final_score}\n")
    elif house_win():
        print(f"House wins with a score of {house_player.final_score} to your {user_player.final_score}\n")
    elif tie():
        print(f"You and the house are tied at {user_player.final_score} points each\n")


def card_shuffling(cards, default, played):
    if len(card_list) < 15:
        cards = default.copy()
        shuffle(cards)
        print("Reshuffling the deck...\n")
        sleep(2.5)
        played.clear()
    return cards


while True:
    house.reset()
    player.reset()
    print("=============================")
    print(f"\t    Round {round_number}")
    print(f"Player: {player.total_wins}     |     House: {house.total_wins}")
    print(f"\t    Ties: {round_number - 1 - (player.total_wins + house.total_wins)}")
    print("=============================")
    gameplay(card_list, house, player, played_cards)
    sleep(2)
    win_tracker(player, house)
    
    round_number += 1
    played_cards.extend(house.cards_in_hand[1:])    
    card_list = card_shuffling(card_list, default_deck, played_cards)
