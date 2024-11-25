from card import Card
import random

class Deck:
    def __init__(self, cards):
        self.cards = cards

    def create_deck(self):
        self.cards = []
        for val in range(2, 15):
            for suit in ("S", "H", "C", "D"):
                imgTag = str(val) + suit + ".png"
                self.cards.append(Card(val, suit, imgTag))

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    # def remove_card(self, val, suit):
    # def add_card(val, suit):
