from card import Card

def create_deck():
    deck = []
    for val in range(2, 15):
        for suit in ("S", "H", "C", "D"):
            deck.append(Card(val, suit))
    return deck