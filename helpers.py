from card import Card

def create_deck():
    deck = []
    for num in range(2, 15):
        for suit in ("spades", "hearts", "clubs", "diamonds"):
            deck.append(Card(suit, num))
    return deck