# TODO: ACCOUNT FOR MULTIPLE ACES IN HAND

class Scoring:
    def __init__(self, cards):
        self.cards = cards
        # We use this to check if an ace has been scored
        self.ace_flag = False
        self.total_score = 0

    def get_score(self):
        for card in self.cards:
            if card.score == "Ace":
                # We check if an ace is in hand, remove it, and note its presence
                self.ace_flag = True
            else:
                # Sums up the rest of the score
                self.total_score += card.score

        if self.total_score <= 10 and self.ace_flag:
            self.total_score += 11
        elif self.total_score >10 and self.ace_flag:
            self.total_score += 1

        return self.total_score

