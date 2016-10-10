for i in range(10000):

    #initializing traingle number
    traingle_number = 0

    #Summing all integers from 1 to i to calculate traingle number
    for j in range(i+1):
        traingle_number += j
    
    #initilized a blank list to append divisors of traingle number
    divisors = []

    #looping through all integers from 1 to traingle number to find its divisors
    for k in range(1,traingle_number+1):
        if traingle_number%k==0:
            divisors.append(k)

    #Stop condiition to print the first solution
    if len(divisors) > 500:
        print(traingle_number)
        break



