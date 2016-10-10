def checkPrime(x):
    isPrime = True
    for i in range(2, int(x**0.5)):
        if x%i==0:
            isPrime = False
    return(isPrime)

def PrimeFactors(x):
    PrimeFactors = []
    firstList = list(range(2, int(x**0.5)))
    for i in firstList:
        if x%i==0 and checkPrime(i):
                PrimeFactors.append(i)
                newList = []
                m = 1
                while i*m < x:
                    newList.append(i*m)
                    m +=1
                firstList = list(set(firstList) - set(newList))
    return(PrimeFactors)

            
PrimeFactors(600851475143)

    
