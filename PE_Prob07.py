'''
def primefinder(x):
    primes = [2]
    i = 3
    while i <= x:
        for j in primes:
            if i%j==0:
                break
        else:
            primes.append(i)
        i += 2
    return(primes)

primes_till_100 = primefinder(100)
'''

primes = [2,3,5,7,9,11,13,17,19]

i = 21

while len(primes) != 10002:
    isPrime = True
    for item in primes:
        if i%item==0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
    i += 2

print(primes[len(primes)-1])
