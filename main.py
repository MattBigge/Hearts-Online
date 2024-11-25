from helpers import create_deck
import random
# from deck import Deck
from card import Card
from player import Player

def setup_deck():
    deck = create_deck()
    random.shuffle(deck)
    return deck[0:13], deck[13:26], deck[26:39], deck[39:52]

hand1,hand2,hand3,hand4 = setup_deck()
ace_space = Card(14, "S")
player_1 = Player("Player 1", hand1, 0)
player_2 = Player("Player 2", hand2, 0)
player_3 = Player("Player 3", hand3, 0)
player_4 = Player("Player 4", hand4, 0)

print(player_1)
print(player_2.cards)
print(player_3.cards)
print(player_4.cards)