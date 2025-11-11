class Scoring:
    def __init__(self, cards):
        self.cards = cards
        # We use this to check if an ace has been scored
        self.no_aces = 0
        self.total_score = 0


    # Done to get the score in the event of one or more aces
    def ace_handling(self, score, aces):
        if score + 10 + aces <= 21 and aces > 0:
            return score + 10 + aces
        else:
            return score + aces


    def get_score(self, card):
        if card.score == "Ace":
            # We check if an ace is in hand and note its presence
            self.no_aces += 1
        else:
            # Sums up the rest of the score
            self.total_score += card.score


    # Function that returns the score of the hand
    # e.g.: [Seven of Hearts, Jack of Spades] returns 17
    def return_score(self):
        self.total_score = 0  # Resets score before counting again
        self.no_aces = 0
        for card in self.cards:
            self.get_score(card)
        # Returns the final code, considering the effect of aces
        return self.ace_handling(self.total_score, self.no_aces)
