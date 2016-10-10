def sumDigitsFacto(x):
    sum = 0
    facto = 1
    for item in range(1,x+1):
        facto *= item
    for item in str(facto):
        sum += int(item)
    return(sum)

print(sumDigitsFacto(100))
