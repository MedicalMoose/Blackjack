from actor import Actor
from time import sleep

class House(Actor):
    def __init__(self):
        super().__init__()
        self.name = "House"


    # We're using the skeleton of the method in the superclass, and tweaking it a bit.
    # POLYMORPHISM!
    def opening_draw(self, card_list):
        for i in range(2):
            self.cards_in_hand.append(card_list.pop())
        print(f"{self.name}: \t{self.cards_in_hand[0]}, ???")


    # Yes - this does count as us making an A.I.
    def house_behavior(self, player_score, card_list):
        self.display_hand()
        house_score = self.score.get_score()
        self.status_check()
        while house_score < player_score and house_score < 17 and self.hit_available:
            sleep(1)
            self.hit(card_list)
            house_score = self.score.get_score()
        self.final_score = house_score
        if house_score >= player_score:
            self.stand()
        elif house_score > 21:
            self.loss_case()
            