from actor import Actor

class Player(Actor):
    def __init__(self):
        # Inherits a bunch of stuff from the Actor class
        super().__init__()
        self.name = "Player"  # Sets the name to Player


    def player_response(self):
        response = input("Hit (h) or Stand (s)?").lower()
        while response not in ["h", "s"]:
            response = input("Hit (h) or Stand (s)? \n").lower()
        return response


    def offer_hit(self, cards_list):
        if self.hit_available:
            response = self.player_response()
        if response == "h":
            self.hit(cards_list)
        else:
            self.stand()
    