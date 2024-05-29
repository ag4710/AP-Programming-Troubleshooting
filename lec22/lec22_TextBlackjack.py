import random

FACES = list(range(2,11)) + ["Jack", "Queen", "King", "Ace"]
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

class Card(object):
    def __init__(self, face, suit):
        assert face in FACES and suit in SUITS
        self.face = face
        self.suit = suit
    def __str__(self):
        article = "a"
        if self.face in ["8","Ace"]:
            article = "an"
        return article+" "+str(self.face)+" of "+self.suit
    def value(self):
        if type(self.face) == int:
            return self.face
        elif self.face == "Ace":
            return 11
        else:
            return 10
        
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face,suit))
        random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()

def hand_value(hand):
    value =0
    for card in hand:
        value += card.value()
    return value

def ask_yesno(prompt):

    while True:
        user_input = input(prompt)
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'")
    

def blackjack():
    deck=Deck()
    dealer =[]
    player =[]

    player.append(deck.draw())
    print("You are dealt", player[0])
    dealer.append(deck.draw())
    print("Dealer is dealt a hidden card")
    player.append(deck.draw())
    print("You are dealt", player[1])
    dealer.append(deck.draw())
    print("Dealer is dealt", dealer[1])
    print("Your total is", hand_value(player))

    while hand_value(player) < 21:
        if not ask_yesno("Would you like another card? (y/n)"):
            break
        
        player.append(deck.draw())
        print("You are dealt", player[-1])
        print("Your total is", hand_value(player))

    if hand_value(player) > 21:
        print("You went over 21! You lost!")
        return -1
    
    print("The dealer's hidden card was", dealer[0])
    while hand_value(dealer) < 17:
        dealer.append(deck.draw())
        print("Dealer is dealt", dealer[-1])
    print("The dealer's total is", hand_value(dealer))

    player_total = hand_value(player)
    dealer_total = hand_value(dealer)
    print("\nYour total is", player_total)
    print("The dealer's total is", dealer_total)

    if dealer_total > 21:
        print("The dealer went over 21! You win!")
        return 1
    
    if player_total > dealer_total:
        print("You win!")
        return 1
    if player_total < dealer_total:
        print("You lost!")
        return -1  
    print("You have a tie!")
    return 0

def game_loop():
    print("Welcome to Blackjack 101!")
    while True:
        blackjack()
        if not ask_yesno("\nWould you like to play again? (y/n) "):
            break

game_loop()