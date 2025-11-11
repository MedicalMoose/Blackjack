from scoring import Scoring

class Actor:
    def __init__(self):
        self.cards_in_hand = []
        self.score = Scoring(self.cards_in_hand)
        self.final_score = 0
        self.hit_available = False
        self.win = False
        self.lost = False
        self.name = ""
        self.total_wins = 0


    def win_case(self):
        self.display_hand()
        print(f"{self.name} hit blackjack!\n")
        self.hit_available = False # Prevents drawing a card after win
        self.win = True


    def loss_case(self):    
        print(f"{self.name} busted!\n")
        self.lost = True
        self.hit_available = False  # Prevents drawing a card after loss


    # Checks to see if the actor has won, lost, or can hit again
    def status_check(self):
        if self.score.return_score() > 21:
            self.loss_case()
        elif self.score.return_score() == 21:
            self.win_case()
        else:
            self.hit_available = True
    
            
    # Handles the opening draw for the actor
    def opening_draw(self, cards, played):
        for card in range(2):  # Draws two cards
            self.cards_in_hand.append(cards.pop())
            played.append(self.cards_in_hand[-1])
        self.status_check()
        if not self.win:
            self.display_hand()
        else:
            self.win_case


    # Gives the ability to draw another card, before checking status of hand
    def hit(self, cards):
        self.cards_in_hand.append(cards.pop())
        if not self.win:
            self.display_hand()
        self.status_check()


    # We're basically just saying "We're done! This is the hand I'm playing"
    def stand(self):
        self.hit_available = False
        self.final_score = self.score.return_score()


    # Prints off the cards the actor has in their hands
    def display_hand(self):
        print(f"{self.name}:\t", end = "")
        for card in self.cards_in_hand:
            # This is why we had the __str__ method in the Cards class
            print(card, end = "\n\t")  # end= " " makes it so all the cards are on the same line
        print()  # New line after printing cards, purely for aesthetics


    def reset(self):
        self.cards_in_hand = []
        self.score = Scoring(self.cards_in_hand)
        self.final_score = 0
        self.hit_available = False
        self.win = False
        self.lost = False
        