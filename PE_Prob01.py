
### A naive approach 

num_3 = [x*3 for x in range(1,1000) if x*3<1000]
num_5 = [x*5 for x in range(1,1000) if x*5<1000]

all_nums = list(set(num_3 + num_5))

sum = 0
for item in all_nums:
    sum += item

print(sum)

## Much faster approach
sum([x for x in range(1001) if x%3==0 or x%5==0])
