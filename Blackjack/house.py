from actor import Actor

class House(Actor):
    def __init__(self):
        super().__init__()
        self.name = "House"


    # We're using the skeleton of the method in the superclass, and tweaking it a bit.
    # POLYMORPHISM!
    def opening_draw(self, card_list):
        for i in range(2):
            self.cards_in_hand.append(card_list.pop())
        self.status_check()
        print(f"{self.name}: {self.cards_in_hand[0]}, ???")


    # Yes - this does count as us making an A.I.
    def house_behavior(self, player_score, card_list):
        self.display_hand()
        house_score = self.score.get_score()
        while house_score < player_score and house_score < 21:
            self.hit(card_list)
            house_score = self.score.get_score()
        if house_score >= player_score and house_score <= 21:
            self.stand()