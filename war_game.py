import deck
import player

class War:
    def __init__(self):
        name1 = input("Player 1: ")
        name2 = input("Player 2: ")
        self.deck = deck.Deck()
        self.p1 = player.Player(name1)
        self.p2 = player.Player(name2)

    # Prints the current play
    def draw(self, p1_name, p1_card, p2_name, p2_card):
        print("{} drew {}, {} drew {}".format(
            p1_name, p1_card, p2_name, p2_card))
    
    # Prints who won the round
    def wins(self, winner):
        print("{} wins this round".format(winner))

    # Returns the winner or print if is a tie
    def winner(self, p1, p2):
        if (p1.wins > p2.wins):
            return (p1.name)
        elif (p1.wins < p2.wins):
            return (p2.name)
        print("It is a tie!")

    # Play the game
    def play_game(self):
        cards = self.deck.cards
        print("\nBegging War!")
        while (len(cards) >= 2):
            usr_input = input("\nInsert 'q' to quit or any other key to play : ")
            if (usr_input == 'q'):
                break
            p1_name = self.p1.name
            p2_name = self.p2.name
            p1_card = self.deck.rm_card()
            p2_card = self.deck.rm_card()
            self.draw(p1_name, p1_card, p2_name, p2_card)
            if (p1_card > p2_card):
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins!".format(win))
