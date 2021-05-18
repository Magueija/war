from random import shuffle
import cards

class Deck:
    # Creates a deck with 52 cards
    # Line-by-line:
    # @12 - suits
    # @13 - values
    # @15 - shuffles deck of cards
    def __init__(self):
        self.cards = []
        for st in range(4):
            for vl in range(2, 15):
                self.cards.append(cards.Card(vl, st))
        shuffle(self.cards)

    # Removes a card from the deck, but if 
    #   the deck is empty returns None
    def rm_card(self):
        if (len(self.cards) == 0):
            return
        return self.cards.pop()
