fib_series = [1, 2]

sum = 0
while fib_series[len(fib_series)-1] < 4000000:
	item = fib_series[len(fib_series)-1]+fib_series[len(fib_series)-2]
	if item%2==0:
		sum += item    	
	fib_series.append(item)

print(sum)
