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


Primes = primefinder(20)

Primes_product = 1

for item in Primes:
    Primes_product *= item

isFound = False
i = 1
while not isFound:
    division = [(Primes_product*i)%x for x in range(1,21) if (Primes_product*i)%x==0]
    if len(division)==20:
        isFound = True
    else:
        i += 1

print(Primes_product*i)
