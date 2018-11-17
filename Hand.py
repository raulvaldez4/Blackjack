class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the deck class
        self.value_list = []  # numerical representation of two cards
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.soft = False  # Determines soft hand (contains Ace) or hard hand (no Ace)

    def add_card(self,card):
        # card passed in here is NOT referencing Card class. Think of it more as a placeholder argument.
        # When using the add_card method further down, this will be passed in from Deck.deal() -> single Card(suit,rank)
        self.cards.append(card)
        self.value_list.append(values[card.rank])
        self.value += values[card.rank]  # returns a value for respective card's rank (.rank is attribute from Card class)

        # Track aces
        if card.rank == 'Ace':
            self.aces += 1
            self.soft = True

    def adjust_for_ace(self):

        # If total value > 21 and I still have an ace
        # Then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


#test_deck = Deck()
#test_deck.shuffle()

# Test Player
#test_player = Hand()
# Deal 1 card from the deck Card(suit,rank)
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)
#print(test_player.value_list)
#print(test_player.soft)
