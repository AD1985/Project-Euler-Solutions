def primefinder(x):
    sum = 2
    primes = [2]
    i = 3
    while i <= x:
        isPrime = True
        for j in primes:
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            sum += i
            primes.append(i)
        i += 2
    return(sum)

print(primefinder(2000000))            

'''
sum = 0
for i in primefinder(2000000):
    sum += i

print(sum)
'''

                
