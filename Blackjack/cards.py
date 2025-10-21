class Cards:
    def __init__(self, suit, rank, score):
        self.suit = suit
        self.rank = rank
        self.score = score

    # String representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"