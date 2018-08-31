primes = 0
factors = [2,3,5,7,9]
results =[]

for x in range(2,20):
    for y in factors:
        if (x%y != 0 or x/y == 1) and x not in results:
            results.append(x)
print(results)
print(f'primes {primes}')


def spy_game(nums):
    detect = ""
    for v in nums:
        detect += str(v)
    return '007' in detect
#asdfs
