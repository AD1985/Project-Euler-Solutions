num = 0
for i in range(1,1001):
    num += (i**i)


#num = reduce(lambda x: x*x, range(1,1001))
print(str(num)[-10:])
