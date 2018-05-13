# Global initial variables ==========================
board = ['#','','','','','','','','','']
playagain = True
# Functions =========================================
# Builds the game board
def buildboard(first=0):
    if first == 0:
        print("\n" * 3)
    # Prints the board updated with values
    print("_" + board[1] + "_|_" + board[2] + "_|_" + board[3] + "_")
    print("_" + board[4] + "_|_" + board[5] + "_|_" + board[6] + "_")
    print("_" + board[7] + "_|_" + board[8] + "_|_" + board[9] + "_")

# Decides what player is X and O
def pickPlayer():
    player1 = ""
    player2 = ""
    # checks to make sure the user enters X or O
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player1, X or O?: ').upper()
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    print(f'Player 1 is: {player1} and Player 2 is: {player2}')
    print('\nAlright! Lets play!')
    print('Player 1 it is your turn!\nTo select a spot enter a number')
    print('left to right 1 2 3 bottom row, 4 5 6 middle, 7 8 9 top ')
    buildboard(1)
    players = (player1,player2)
    return players

def maingame():
    player = 0
    turns = 0
    gameon = True

    players = pickPlayer()
    while gameon:
        tryagain = True
        marker = input('Select a location: ')

        if board[int(marker)] != '':
            while tryagain:
                marker = input('Spot is already taken, try again: ')
                if board[int(marker)] == '':
                    tryagain = False

        board[int(marker)] = players[player]


        if turns == 9:
            gameon = False
        buildboard()
        if player == 0:
            player += 1
        else:
            player -= 1

maingame()
while playagain:
    answer = input('Play again?: ').upper()
    if answer != "Y":
        playagain = False
    else:
        maingame()

'''
player one goes first and puts a marker down
Do a check if the game is won

while gameOn is true:
    put marker down based on input number
    check to see if the game is won
    keep going until the board is full or these combos are fulfilled
        123,456,789 rows
        147,258,369 columns
        159,357 diagonally
    change gameover to true and break
ask to play again
    if yes change the board to blank and ask the player X or O
'''
