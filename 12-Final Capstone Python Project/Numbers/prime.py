# take a number divide by 2
# if mod 0 >> add 2 to list
# keep going until can't 

n = input("Enter a number to see its prime factorizations: ")
try:
    n = int(n)
except:
    print(n + ' is not a number!')
    exit(0)

primes = list()

for i in range(2,n):
    num = n - i
    if n % num == 0 and num != 1:
        primes.append(num)
print(primes)