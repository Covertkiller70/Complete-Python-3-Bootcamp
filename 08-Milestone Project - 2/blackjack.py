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
        self.push = False
        self.stillin = True
        self.split= False

    #def __str__(self):
    #    return self.name + " has $" + str(self.account - self.bet) + " left"

    def sethand(self,hand):
        self.hand = hand

    def showhand(self):
        handtxt = ''
        for card in self.hand:
            handtxt += f"[{card.value} of {card.suite}] "
        return handtxt

    def win(self,chips):
        self.account += chips
        print(f"{self.name} Account balance: ${self.account}")

    def lose(self,chips):
        if self.account - chips < 10:
            self.stillin = False
            print(f"Player {self.name} is out of the game!")
        else:
            self.account -= chips
            print(f"{self.name} Account balance: ${self.account}")

class Dealer:
    def __init__(self):
        self.account = 10000000
        self.soft = False
        self.blackjack = False
    def __str__(self):
        print(f"Dealer has [{self.hand[0]}] and a [{self.hand[1]}]")
    def sethand(self,hand):
        self.hand = hand
        print(f"Dealer has [{self.hand[0]}], and one unknown")
    def showhand(self):
        handtxt = ''
        for card in self.hand:
            handtxt += f"[{card.value} of {card.suite}] "
        return handtxt

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
                player.bet = bet
                print(f"{player.name} bets ${str(bet)}, ${str(player.account - player.bet)} left\n")
                break
            elif bet < 10:
                print("$10 minimum bets! Try again with a higher bet...")
            else:
                print(f"Bet must be less than ${str(player.account)}!")
        except:
            print("Bet must be a number")

# Figures out the hand value and returns total
def gethandvalue(player, hand):
    total = 0
    # gets the total of the hand as is
    for card in hand:
        if card.value in ("Jack","Queen","King"):
            total += 10
        elif card.value == "Ace":
            total += 11
        else:
            total += int(card.value)
    # If the hand has Aces and is over 21, change the Aces to 1
    for card in hand:
        if card.value == "Ace" and total > 21:
            total -= 10
    return total

# Checks the given cards, sees if a condition is met
# Need to add insurance
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
                if (dtotal > total and dtotal < 21) or total > 21 or (dtotal == 21 and total != 21):
                    print(f"{players[player].name} lost ${players[player].bet}")
                    players[player].lose(players[player].bet)
                    players[player].push = False
                elif (21 > total > dtotal) or (21 > total and dtotal > 21) or (total == 21 and dtotal != 21):
                    print(f"{players[player].name} won ${players[player].bet * 2}")
                    players[player].win(players[player].bet * 2)
                    players[player].push = False
                elif dtotal == total:
                    print(f"{players[player].name} pushes")
                    players[player].push = True

# Incites action for player for their turn
# Need to account for splits
def playeraction(players,thedeck):
    for player in players:
        while True:
            print(f"{players[player].name} has {players[player].showhand()}, count is {gethandvalue(players[player], players[player].hand)}")
            action = input(f"{players[player].name}, hit or stay?: ")
            if action in ("HIT", "hit", "Hit", "1","H","h"):
                players[player].hand.append(thedeck.dealcard())
                total = gethandvalue(players[player], players[player].hand)
                print(f"\n{players[player].name} pulls a {players[player].hand[-1]}, count is {total}")
                if total > 21:
                    print(f"{players[player].name} busts at {total}\n")
                    break
                elif total == 21:
                    print(f"{players[player].name} got a Blackjack!\n")
                    break
            elif action in ("stay","STAY","Stay","0","s","S"):
                print(f"{players[player].name} stays at {gethandvalue(players[player], players[player].hand)}\n")
                break

# Dealers actions
def dealeraction(dealer, thedeck):
    while True:
        print(f"Dealer has {dealer.showhand()}, count is {gethandvalue(dealer, dealer.hand)}")
        total = gethandvalue(dealer, dealer.hand)
        if total > 21:
            print(f"Dealer busts at {total}")
            break
        elif total == 21:
            print(f"Dealer gets Blackjack!")
            break
        elif total <= 16:
            print("Dealer hits...")
            dealer.hand.append(thedeck.dealcard())
        elif total >= 17:
            print(f"Dealer stays, count is {total}")
            break

# Check for players remaining
def checkremainingplayers(players):
    return players

# =========== Main code running =============
# ===========================================
# Intro message, deck setup and dealer creation
players = getplayers()
thedeck = Deck()
thedeck.shuffle()
dealer = Dealer()
while True:
    for player in players:
        if players[player].push == False:
            placebet(players[player])
        players[player].sethand(thedeck.dealhand())
    dealer.sethand(thedeck.dealhand())
    checkcards(players,dealer,first=True)
    playeraction(players, thedeck)
    dealeraction(dealer,thedeck)
    checkcards(players,dealer,first=False)

    choice = input("Do you want to play again? (y/n): ")
    if choice in ("n","N"):
        break
