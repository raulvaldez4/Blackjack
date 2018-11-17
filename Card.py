class Card:
    """
    Card class that holds suit and rank for one card. --> Card(suit,rank)
    Takes in a suit,rank and returns a string i.e "Two of hearts"
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)


#print(Card('Hearts','Two'))