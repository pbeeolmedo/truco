"""

This module contains code from
Think Python: an Introduction to Software Design
Allen B. Downey

"""

import random

class Card(object):
    """represents a standard playing card."""

    suit_names = ["Basto", "Oro", "Copa", "Espada"]
    rank_names = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

    def __init__(self, suit= 1, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} de {self.rank}"

print(Card().suit_names)
print(Card(suit = 1, rank = 10))

class Deck(object):
    """represents a deck of cards"""
    
    def __init__(self):
        self.cards = []
        for suit in Card().suit_names:
            for rank in Card().rank_names:
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """add a card to the deck"""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """remove and return a card from the deck.
        By default, pop the last card."""
        return self.cards.pop(i)

    def shuffle(self):
        """shuffle the cards in this deck"""
        random.shuffle(self.cards)

    def sort(self):
        """sort the cards in ascending order"""
        self.cards.sort()
    
    def move_cards(self, hand, num):
        """move the given number of cards from the deck into the Hand"""
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """represents a hand of playing cards"""
    
    def __init__(self, label=''):
        self.label = label
        self.cards = []


def find_defining_class(obj, meth_name):
    """find and return the class object that will provide 
    the definition of meth_name (as a string) if it is
    invoked on obj.
    """
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    pass