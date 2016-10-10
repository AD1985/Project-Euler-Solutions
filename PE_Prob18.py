table = [[int(x) for x in x.split()] for x in open("/home/fractaluser/Documents/PE18.txt").readlines()]

for row in range(len(table)-1,0,-1):
        for item in range(0,row):
                table[row-1][item] += max(table[row][item], table[row][item+1])

print(table[0][0])
