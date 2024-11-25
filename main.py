from helpers import create_deck
import random
# from deck import Deck
from card import Card
from player import Player

deck = []

def setup_deck():
    deck = create_deck()
    random.shuffle(deck)
    return deck
        
def split_deck_to_players():
    return deck[0:13], deck[13:26], deck[26:39], deck[39:52]

cards = setup_deck()

hand1,hand2,hand3,hand4 = split_deck_to_players()
hand1 = deck[0:13]
ace_space = Card("spades", 14)
player_1 = Player("Player 1", hand1)
player_2 = Player("Player 2", hand2)
player_3 = Player("Player 3", hand3)
player_4 = Player("Player 4", hand4)

print(player_1.cards)
print(ace_space)
print(player_2.cards)
print(player_3.cards)
print(player_4.cards)