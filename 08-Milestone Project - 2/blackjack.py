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
        self.bet = 0
        self.stillin = True
        self.soft = False
        self.split= False
    
    def __str__(self):
        return self.name + " has $" + str(self.account) + " left" 
 
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
        self.soft = False
        self.blackjack = False
    def sethand(self,hand):
        self.hand = hand
        print(f"Dealer has [{self.hand[0]}], and one unknown")
    def showhand(self):
        print(f"Dealer has [{self.hand[0]}] and a [{self.hand[1]}]")

# === Methods and functionss ===
# Gets number of players playing this round
def getplayers():
    while True:
        try:
            numofplayers = int(input("Number of players at the table?: ")) + 1
            players = {}
            for i in range(1, numofplayers):
                players['player' + str(i)] = Player()
            break
        except:
            print("Enter a number...")
    return players

# Players make bets
def placebet(player):
    while True:
        try:
            bet = int(input(f"{player.name} enter a number to bet: "))
            if (player.account - bet) > 0:
                player.account -= bet
                player.bet = bet
                print(f"{player.name} bets ${str(bet)}, ${str(player.account)} left")
                break
            else:
                print(f"Bet must be less than ${str(player.account)}!")
        except:
            print("Bet must be a number")

# Figures out the hand value and returns total
def gethandvalue(player, hand):
    total = 0
    for card in hand:
        if card.value == "Ace":
            player.soft == True
        if card.value in ("Ace", "Jack","Queen","King"):
            total += 10
        else:
            total += int(card.value)
    return total

# Checks the given cards, sees if a condition is met
def checkcards(players,dealer,first):
    dtotal = gethandvalue(dealer, dealer.hand)
    for player in players:
        if players[player].stillin == True:
            total = gethandvalue(players[player], players[player].hand)
            if first == True:
                if total == 21 and dtotal != 21:
                    players[player].win(players[player].bet * 3)
                    players[player].stillin = False
                    print(f"{players[player].name} got a black jack! {players[player].name} won ${players[player].bet * 3}")
                if dtotal == 21 and total != 21:
                    players[player].lose(players[player].bet)
                    print(f"{players[player].name} lost ${players[player].bet}")   
            if first == False:
                if total > dtotal or (total == 21 and dtotal != 21):
                    players[player].win(players[player].bet * 2)
                    print(f"{players[player].name} won ${players[player].bet * 2}")
                elif dtotal > total:
                    players[player].lose(players[player].bet)
                    print(f"{players[player].name} lost ${players[player].bet}")

# Incites action for player for their turn
# need to add in soft hits
def playeraction(players,thedeck):
    for player in players:
        while True:     
            action = input(f"{players[player].name}, hit or stay?: ")
            if action == "Hit" or action == "hit":
                players[player].hand.append(thedeck.dealcard())
                print(f"{players[player].name} pulls a {players[player].hand[-1]}")
                total = gethandvalue(players[player], players[player].hand)
                if total > 21:
                    players[player].stillin = False
                    print(f"{players[player].name} busts at {total}")
                    break
                else:
                    print(f"count is {total}")
            elif action == "Stay" or action == "stay":
                print(f"{players[player].name} stays at {gethandvalue(players[player], players[player].hand)}")
                break

# =========== Main code running =============
# ===========================================
# Intro message, deck setup and dealer creation
thedeck = Deck()
thedeck.shuffle()
players = getplayers()
dealer = Dealer()
for player in players:
    placebet(players[player])
    players[player].sethand(thedeck.dealhand())
dealer.sethand(thedeck.dealhand())
# Check if anyone got a blackjack
checkcards(players,dealer,first=True)
playeraction(players, thedeck)
# dealer shows second card
# dealer starts hitting/staying
# hits on 16 stays on 17, hits on a soft 17 
# Compare cards again
# Pay out winners, take from losers