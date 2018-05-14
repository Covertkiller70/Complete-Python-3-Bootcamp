# Builds the game board ========================================================
def buildboard(first=0):
    if first == 0:
        print("\n" * 3)
    # Prints the board updated with values
    print("_" + board[1] + "_|_" + board[2] + "_|_" + board[3] + "_")
    print("_" + board[4] + "_|_" + board[5] + "_|_" + board[6] + "_")
    print("_" + board[7] + "_|_" + board[8] + "_|_" + board[9] + "_")

# Decides what player is X and O ===============================================
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
    players = ('',player1,player2)
    return players

# Check rows ===================================================================
def checkwinner(players):
    player1 = players[1]
    player2 = players[2]
    check = ""
    # for loop will not work here because its detecting XXX or OOO from one row to the next
    # need to make this watch for one row at a time
    for i in board:
        check += str(i)
    if player1*3 in check:
        print('won by rows')
        return 1
    elif player2*3 in check:
        print('won by rows')
        return 2
    elif board[1::3] == list(player1)*3 or board[2::3] == list(player1)*3 or board[3::3] == list(player1)*3:
        print('won by column')
        return 1
    elif board[1::3] == list(player2)*3 or board[2::3] == list(player2)*3 or board[3::3] == list(player2)*3:
        print('won by column')
        return 2
    elif str(board[1] + board[5] + board[9]) == player1*3 or str(board[3] + board[5] + board[7]) == player1*3:
        print('won by diagonal')
        return 1
    elif str(board[1] + board[5] + board[9]) == player2*3 or str(board[3] + board[5] + board[7]) == player2*3:
        print('won by diagonal')
        return 2
    else:
        return 0

'''
[X,'','O','','XO','','O','',X]
159,357 diagonally
'''

# main game ====================================================================
def maingame():
    player = 1
    turns = 0
    gameon = True
    winner = 0

    # Have player pick X or O
    players = pickPlayer()

    while gameon:
        tryagain = True
        # Get the marker from the player
        marker = input(f'Player{player}, Select a location: ')
        # Make sure that spot isn't taken
        if board[int(marker)] != '':
            while tryagain:
                marker = input('Spot is already taken, try again: ')
                if board[int(marker)] == '':
                    tryagain = False
        # place the marker on the board
        board[int(marker)] = players[player]
        # rebuild the board
        buildboard()
        # check to see if there is a winner
        winner = checkwinner(players)
        # check to see if all the spots are used up or if there is a winner
        if turns == 9 or winner != 0:
            if winner == 1 or winner == 2:
                print(f'Player{winner} won the game!')
            else:
                print('Tie game!')
            gameon = False
        else:
            # Alternate to the next player
            if player == 1:
                player += 1
            else:
                player -= 1
        # Tick the turn over one
        turns += 1

# Main running program =========================================================
board = ['#','','','','','','','','','']
playagain = True
maingame()
# See if players want to play again
while playagain:
    answer = input('Play again?: ').upper()
    if answer != "Y":
        playagain = False
        print('Thanks for playing!\nSee you next time!')
    else:
        board = ['#','','','','','','','','','']
        maingame()