from actor import Actor

class Player(Actor):
    def __init__(self):
        # Inherits a bunch of stuff from the Actor class
        super().__init__()
        self.name = "Player"  # Sets the name to Player


    def player_response(self):
        response = input("Hit (h), Stand (s), or View Cards (v)? \n").lower()
        while response not in ["h", "s", "v"]:
            response = input("Hit (h), Stand (s), or View Cards (v)? \n").lower()
        print("")  # Whitespace
        return response


    def offer_hit(self, cards, played):
        if self.hit_available:
            response = self.player_response()
        if response == "h":
            self.hit(cards)
        elif response == "v":
            self.card_view(cards, played)
        else:
            self.stand()
    

    # This is just so I can get the sign in front of the odds
    # I just think it's pretty neat
    def odds_printing(self, rank_odds, expected_odds, count):
        if rank_odds >= expected_odds:
            print(f"Odds of being drawn: +{rank_odds - expected_odds:.2%}\n")
        elif rank_odds < expected_odds and count > 0:
            print(f"Odds of being drawn: -{expected_odds - rank_odds:.2%}\n")
        elif count == 0:
            print(f"Odds of being drawn: 0.00%\n")
        elif rank_odds == expected_odds:
            print(f"Odds of being drawn: {expected_odds:.2%}\n")


    def count_ranks(self, counts, value, no_ranks):
        if counts[value] > 0:
                no_ranks += 1
        return no_ranks


    def card_view(self, cards, played):
        rank_odds = 0
        cards_left = 52
        total_ranks = 0
        # Resets whenever called
        card_counts = {
                        "2" : 4,
                        "3" : 4,
                        "4" : 4,
                        "5" : 4,
                        "6" : 4,
                        "7" : 4,
                        "8" : 4,
                        "9" : 4,
                        "10" : 4,
                        "Jack" : 4,
                        "Queen" : 4,
                        "King" : 4,
                        "Ace" : 4
                      }
        
        # Removes played cards from the counts
        for playing_card in played:
            card_counts[playing_card.rank] -= 1
            cards_left -= 1
        
        # Tallies the number of ranks that can still be drawn
        for rank in card_counts:
            total_ranks = self.count_ranks(card_counts, rank, total_ranks)

        # This actually hurt my head a bit when I wrote it
        # I had to play Troublemaker by Weezer to deal with it
        # This isn't even that confusing
        # I might be mentally challenged
        mean_count = cards_left / total_ranks
        expected_odds = mean_count / len(cards)

        for rank, count in card_counts.items():
            print(f"{rank}: {count}")
            rank_odds = count / len(cards)
            self.odds_printing(rank_odds, expected_odds, count)
