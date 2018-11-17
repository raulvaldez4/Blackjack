class Chips:
    def __init__(self):
        self.total = 100  # This can be a default value or supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet * 2

    def lose_bet(self):
        self.total -= self.bet
