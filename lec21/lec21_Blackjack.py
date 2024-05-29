def hand_value(hand):
    total = 0
    for card in hand:
        total += card.value
    return total

def card_string(card):
    article = "a " 
    if card.face in [8, "Ace"]:
        article = "an "
    return article + str(card.face) + " of " + card.suit

class Card(object):
    """A Blackjack card."""
    pass

c = Card()  # Create Card object 
c.face = "Ace"  # Set attributes of the card 
c.suit = "Spades"
c.value = 11

card1 = Card() 
card1.face = "Ace" 
card1.suit = "Spades" 
card1.value = 11 
card2 = Card() 
card2.face = 2 
card2.suit = "Clubs" 
card2.value = 2

print(card_string(card1))
print(card_string(card2))