num = 0
for i in range(123456789, 9876543210):
    if len(str(i)) != len(set(str(i))):
        next
    else:
        num = num + 1
    if num == 1000000:
        print(i)
        break

    
