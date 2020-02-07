n = input('Enter a number to see its prime factors: ')

try:
    n = int(n)
except:
    print(n + ' is notn = n/2 a number!')

primes = list()
while(n%2 == 0):
    n = int(n/2)
    primes.append(n)

if len(primes) == 0:
    primes.append(n)
else:
    primes.append(2)
 
print(primes)