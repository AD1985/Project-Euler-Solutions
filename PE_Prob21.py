def sumDivisors(x):
    sum = 0
    for item in range(1,int(x/2)+1):
        if x%item==0:
            sum += item
    return(sum)

sum = 0
for item in range(1, 10001):
    if sumDivisors(sumDivisors(item))==item:
        sum += item
