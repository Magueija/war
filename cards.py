class Card:
    # The first two values are None for the index = "number"
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "king", "Ace")
    suits = ("spades", "hearts", "diamonds", "clubs")

    # suit_idx and value_idx are ints - index to suits or values
    def __init__(self, vl, st):
        self.value_idx = vl
        self.suit_idx = st

    # Method to compare two objects (>)
    def __gt__(self, card2):
        if (self.value_idx > card2.value_idx):
            return True
        elif (self.value_idx == card2.value_idx
            and self.suit_idx > card2.suit_idx):
                return True
        return False

    # Method to compare two objects (<)
    def __lt__(self, card2):
        if (self.value_idx < card2.value_idx):
            return True
        elif (self.value_idx == card2.value_idx
            and self.suit_idx < card2.suit_idx):
                return True
        return False

    # On print Card
    def __repr__(self):
        return (self.values[self.value_idx] + " of " \
            + self.suits[self.suit_idx])
