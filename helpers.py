from card import Card

def create_deck():
    cards = []
    for val in range(2, 15):
        for suit in ("S", "H", "C", "D"):
            cards.append(Card(val, suit))
    return cards