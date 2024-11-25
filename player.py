from card import Card
from deck import Deck

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        
    def __str__(self):
        return f"{self.name} has {self.cards} in hand"