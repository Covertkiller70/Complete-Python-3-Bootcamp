'''
Rules of the game
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

from random import randint

def playgame():
    num2guess = randint(1, 100)
    guesses = 0
    correct = True
    while correct:
        guess = input('Enter your guess: ')
        try:
            guess = int(guess)
            if guess > 100 or 1 > guess:
                print('Guess must be within 1 and 100')
            else:
                if num2guess == guess:
                    correct = False
                    print(f'Yay! You Win!!!\nNumber of tries: {guesses}')
                elif abs(guess - num2guess) <= 10:
                    if abs(guess - num2guess) <= 5:
                        print('HOT! Very HOT!')
                    else:
                        print('Warmer...')
                elif abs(guess - num2guess) >= 10:
                    if abs(guess - num2guess) >= 50:
                        print('Icy Cold!!!')
                    else:
                        print('Colder...')
                guesses += 1
        except ValueError:
            print('Guess must by a number!')

# Intro and instructions
print('Welcome to the random number game!\nHere is how to play:\nGuess a number between 1 and 100\n\nWhen your guess is less than:')
print('\t10 numbers away you are warm\n\t5 numbers away is Hot\n\tover 10 numbers away is cold\n\t50 numbers away you are icy cold!')
print('Happy hunting!\n')
# initial game run
playgame()
again = input('Play again? Y/N')
if again.upper() == 'Y':
    playgame()
else:
    print('Thanks for playing! See you next time!')
