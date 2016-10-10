number = 2
cum_sum = 0
while number < 1000000:
    sum = 0
    for item in str(number):
        sum += int(item)**5
    if sum == number:
        cum_sum += number
    number += 1

print(cum_sum)
