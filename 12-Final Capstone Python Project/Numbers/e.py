import math

e = str(math.e)
end = len(e) - 1 
nth = input('How far back e do you want to go? 1-' + str(end) + ': ')

try:
    nth = int(nth)
except: 
    print(str(nth) + ' is not a number!')
    exit(0)

if nth > 0 and nth < len(e):    
    print(e)
    if nth == 1:
        print(e[0])
    else:        
        space = ''
        for i in range(0, nth):
            space += ' '
        print(space + e[nth])
else:
    print('Enter a number between 1 and ' + str(end) + '!')