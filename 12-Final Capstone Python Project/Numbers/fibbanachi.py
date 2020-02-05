end = input('How far do you want to go?! (Enter a number): ')

try:
    end = int(end)
except:
    print(end + ' is not a number!')
    exit(0)

seq = ''

# Need to know what is the last fib number
# Need to know the second to last fib
# Current fib = last + 2nd2last 

seq = list()
for i in range(0, end+1):
    seq.append(i)

print(seq)