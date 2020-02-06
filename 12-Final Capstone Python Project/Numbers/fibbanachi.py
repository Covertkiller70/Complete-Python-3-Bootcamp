n = input('Enter a number of times to run: ')

try:
    n = int(n)
except:
    print(n + ' is not a number!')
    exit(0)
seq = list()
for i in range(0,n+1):
    if i > 1:
        last1 = seq[-1]
        last2 = seq[-2]
        seq.append(last1+last2)
    else:
        seq.append(i)
print(seq)