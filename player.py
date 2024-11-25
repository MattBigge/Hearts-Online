from card import Card
from deck import Deck
from termcolor import colored

class Player:
    def __init__(self, name, cards, score):
        self.name = name
        self.cards = cards #cards in hand
        self.score = score #score, game ends when a player(s) get above 100pts, lowest score wins
        
    def __str__(self):
        return f"{self.name} has {self.cards} in hand and their score is {self.score}"

    def prompt_card(self):
        card = input("Type card to play: {format: number/suit")
        # check if card is in hand
        # remove

    def check_if_card_in_hand(self, card):
        for c in self.cards:
            if c == card:
                return True
        return False

    def remove_card(self, card):
        for c in self.cards:
            if c == card:
                self.cards.remove(c)
                break