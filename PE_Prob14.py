def chainLength(x):
    n = 1
    while x != 1:
        if x%2==0:
            x = x/2
        else:
            x = 3*x + 1
        n += 1
    return(n)


longLength = 1
y = 13

allnums = {}

while y < 1000000:
    temp = chainLength(y)
    allnums[temp] = y 
    if temp > longLength:
        longLength = temp
    y += 1

print(allnums[longLength])
