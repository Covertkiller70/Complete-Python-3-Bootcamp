# Deck object: cards list
# Card Object: Suite, Value
import random
suites = ("Clubs", "Hearts", "Spades", "Diamonds")
values = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

class Deck:
    def __init__(self):
        self.deck = []
        for _ in range(random.randint(6,8)):  
            for suit in suites:
                for card in values:
                    card = Card(card,suit)
                    self.deck.append(card)
    def __str__(self):
        return str(len(self.deck)) + " cards remaining..."

    def shuffle(self):
        random.shuffle(self.deck)

    def dealhand(self):
        hand = [self.deck.pop(0), self.deck.pop(0)]
        return hand
    
    def dealcard(self):
        return self.deck.pop(0)

class Card:
    def __init__(self, value, suite):
        self.suite = suite
        self.value = value
    def __str__(self):
        return str(self.value) + " of " + self.suite

class Player:
    def __init__(self):
        self.name = input("Enter your playername: ")
        self.account = 100
        self.enabled = True
    def __str__(self):
        return self.name + " has $" + str(self.account) + " left" 
    def bet(self):
        while True:
            try:
                bet = int(input(f"{self.name} enter a number to bet: "))
                if (self.account - bet) > 0:
                    self.account -= bet
                    print(f"{self.name} bets ${str(bet)}, ${str(self.account)} left")
                    break
                else:
                    print(f"Bet must be less than ${str(self.account)}!")
            except:
                print("Bet must be a number")
    
    def sethand(self,hand):
        self.hand = hand
        print(f"{self.name} was delt a [{self.hand[0]}] and a [{self.hand[1]}]")
    
    def win(self,chips):
        self.account += chips
    
    def lose(self,chips):
        if self.account - chips < 0:
            self.enabled = False
            return (f"Player {self.name} is out of the game!")
        else:
            self.account -= chips

class Dealer:
    def __init__(self):
        self.account = 10000000
    
    def sethand(self,hand):
        self.hand = hand
        print(f"Dealer has [{self.hand[0]}], and one unknown")
    def showhand(self):
        print(f"Dealer has [{self.hand[0]}] andß a [{self.hand[1]}]")

# Methods and functionss
def playeraction(player,thedeck):
    action = input(f"{player.name}, hit or stay?: ")
    if action == "Hit" or action == "hit":
        player.hand.append(thedeck.dealcard())
        for i in player.hand:
            print(i.value)

def cardcheck():
    pass


# =========== Main code running =============
# ===========================================
thedeck = Deck()
thedeck.shuffle()

while True:
    try:
        numofplayers = int(input("Number of players at the table?: ")) + 1
        players = {}
        for i in range(1, numofplayers):
            players['player' + str(i)] = Player()
        break
    except:
        print("Enter a number...")

for player in players:
    players[player].sethand(thedeck.dealhand())