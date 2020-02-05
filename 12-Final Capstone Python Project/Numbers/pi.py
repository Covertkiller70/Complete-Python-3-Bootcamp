import math

pi = str(math.pi)
end = len(pi) - 1 
nth = input('How far back pi do you want to go? 1-' + str(end) + ': ')

try:
    nth = int(nth)
except: 
    print(str(nth) + ' is not a number!')
    exit(0)

if nth > 0 and nth < len(pi):    
    print(pi)
    if nth == 1:
        print(pi[0])
    else:
        space = ''
        for i in range(0, nth):
            space += ' '
        
        print(space + pi[nth])
else:
    print('Enter a number between 1 and ' + str(end) + '!')