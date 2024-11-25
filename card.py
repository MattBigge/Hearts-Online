class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        
    def __str__(self):
        return f"{self.val}{self.suit}"