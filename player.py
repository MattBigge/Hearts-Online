from card import Card
from deck import Deck

class Player:
    def __init__(self, name, cards, score):
        self.name = name
        self.cards = cards
        self.score = score
        
    def __str__(self):
        return f"{self.name} has {self.cards} in hand and their score is {self.score}"

