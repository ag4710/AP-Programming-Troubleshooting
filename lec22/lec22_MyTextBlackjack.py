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
    """Already defined __init__ and value methods"""
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


num_players = 2
deck = Deck()
hands = [] # A list of lists (one for each player)

for j in range(num_players): 
    hands.append([])

for i in range(2):
    for j in range(num_players): 
        card = deck.draw() 
        hands[j].append(card)
        if (j == 0):
            print(f"You ard dealt {card}")
        else:
            if (i==0):
                print(f"Dealer is dealt a hidden card")
            else:
                print(f"Dealer is dealt {card}")

print ("Your total is %d" % (hand_value(hands[0])))

print()
nextGame = input("Would you like another card? (y/n) ")
endGame = False

while (nextGame == "y"):
    for j in range(num_players): 
        card = deck.draw() 
        hands[j].append(card)
        if (j == 0):
            print(f"You ard dealt {card}")
        else:
            print(f"Dealer is dealt {card}")
    print ("Your total is %d" % (hand_value(hands[0])))
    if (hand_value(hands[0]) > 21):
        endGame = True
        print("You went over 21! You lost!")
        print(f"The dealer's hidden card was {hands[1][0]}")
        print ("The dealer's total is %d" % (hand_value(hands[1])))
        break

    if (hand_value(hands[1]) > 21):
        endGame = True
        print("Dealer went over 21! You Win!")
        print(f"The dealer's hidden card was {hands[1][0]}")
        print ("The dealer's total is %d" % (hand_value(hands[1])))
        break

    print()
    nextGame = input("Would you like another card? (y/n) ")

if (endGame != True):
    print(f"The dealer's hidden card was {hands[1][0]}")
    print ("The dealer's total is %d" % (hand_value(hands[1])))
    print ("Your total is %d" % (hand_value(hands[0])))

    if (hand_value(hands[0]) > hand_value(hands[1])):
        print("You win!")
    else:
        print("You lost!")
