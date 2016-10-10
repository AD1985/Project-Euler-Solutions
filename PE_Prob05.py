i = 2*3*5*7*11*13*17*19

a = [2,3,5,7,11,13,17,19]

isFound = True
for j in a:
    newList = [int((i*j)%x) for x in range(1,21) if int((i*j)%x)==0]
    if len(newList)==20:
        print(i*j)

