from card import Card
import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
        
    def create_deck(self):
        cards = []
        for num in range(2, 14):
            for suit in ("spades", "hearts", "clubs", "diamonds"):
                self.cards.append(Card(num,suit))
        print("added cards")

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards

    # def remove_card(self, val, suit):
    # def add_card(val, suit):
