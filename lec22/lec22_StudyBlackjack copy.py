import random

def hand_value(hand):
    total = 0
    for card in hand:
        total += card.value()
    return total

def card_string(card):
    article = "a " 
    if card.face in [8, "Ace"]:
        article = "an "
    return article + str(card.face) + " of " + card.suit

FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class Card(object):
    """A Blackjack card."""
    """Already defined __init__ and value methods and other methods"""
    # def string(self): 
    #     article = "a "
    #     if self.face in [8, "Ace"]:
    #         article = "an "
    #     return (article + str(self.face) + " of " + self.suit)
    def __eq__(self, rhs):
        return (self.face == rhs.face and self.suit == rhs.suit)
    
    def __ne__(self, rhs):
        return not self == rhs

    def __str__(self): 
        article = "a "
        if self.face in [8, "Ace"]:
            article = "an "
        return (article + str(self.face) + " of " + self.suit)
    
    def __init__(self, face, suit):
        assert face in FACES and suit in SUITS 
        self.face = face
        self.suit = suit

    def value(self): # method of Card
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10


class Deck(object):
    """A deck of cards."""
    def __init__(self):
        "Create a deck of 52 cards and shuffle them."
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)
    
    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop()

num_players = 3
num_cards = 5 
deck = Deck()
hands = [] # A list of lists (one for each player)

for j in range(num_players): 
    hands.append([])

for i in range(num_cards):
    for j in range(num_players): 
        card = deck.draw() 
        hands[j].append(card)
        print("Player", j+1, "draws", card)

for j in range(num_players):
    print ("Player %d's hand (value %d):" % (j+1, hand_value(hands[j])))
    for card in hands[j]:
        print (" ", card)

print()
print(Card(8, 'Diamonds') == Card(8, 'Diamonds'))
print(Card(8, 'Diamonds') != Card(8, 'Diamonds'))
