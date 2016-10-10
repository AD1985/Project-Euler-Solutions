dec = "0."
i=1
while len(dec)<1000100:
    dec = dec + str(i)
    i = i + 1


print(int(dec[2])*int(dec[11])*int(dec[101])*int(dec[1001])*int(dec[10001])*int(dec[100001])*int(dec[1000001]))
