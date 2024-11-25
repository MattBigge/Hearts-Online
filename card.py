from termcolor import colored

class Card:
    def __init__(self, val, suit, imgTag):
        self.val = val
        self.suit = suit
        self.imgTag = imgTag
        
    def __str__(self):
        return f"{self.val}{self.suit}"

    def __repr__(self):
        if self.suit == "H" or self.suit == "D":
            return colored(f"{self.val}{self.suit}", 'red')
        return colored(f"{self.val}{self.suit}", 'light_grey', "on_black")

