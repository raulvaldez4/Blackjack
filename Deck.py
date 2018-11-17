class Deck:
    """
    Holds 52 card deck
    """
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                # Nested loop appends all 52 cards to self.deck which was an empty list

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()  # Prints out the text representation of card then appends to deck_comp
            # 52 card deck in text format: "Two of hearts" "Three of spades" etc.
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()  # Grab this deck attribute from Deck class and then pop off & assign to
        # single_card
        return single_card

#test_deck = Deck()
#test_deck.shuffle()
#deal()
#print(test_deck)
