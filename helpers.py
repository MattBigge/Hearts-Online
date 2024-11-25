from card import Card

def create_deck():
    cards = []
    for val in range(2, 15):
        for suit in ("S", "H", "C", "D"):
            imgTag = str(val) + suit + ".png"
            cards.append(Card(val, suit, imgTag))
    return cards