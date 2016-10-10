def WordNumber(x):
    if x < 0:
        return("Negative numbers are not accepted.")
    if int(x) != x:
        return("Decimals or characters are not accepted.")
    first20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first20inwords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    multi10 = [20, 30, 40, 50, 60, 70, 80, 90]
    multi10inwords = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    length = len(str(x))
    x = int(x)
    
    if x > 1000:
        return("Number above one thousand is not allowed.")
    elif x==1000:
        return("One Thousand")
    elif length==3:
        x1 = int(str(x)[0])
        x2 = int(str(x)[1])
        x3 = int(str(x)[2])
        if x2==0 and x3==0:
            return(first20inwords[first20.index(x1)]+" Hundred")
        elif int(str(x)[1:]) in first20:
            return(first20inwords[first20.index(x1)]+" Hundred and "+first20inwords[first20.index(int(str(x)[1:]))])
        elif int(str(x)[1:]) in multi10:
            return(first20inwords[first20.index(x1)]+" Hundred and "+multi10inwords[multi10.index(int(str(x)[1:]))])
        else:
            x2=int(str(x2)+"0")
            return(first20inwords[first20.index(x1)]+" Hundred and "+multi10inwords[multi10.index(x2)]+" "+first20inwords[first20.index(x3)])
    elif length==2 and x not in first20 and x not in multi10:
        x1 = int(str(x)[0])
        x2 = int(str(x)[1])
        x1 = int(str(x1)+"0")
        return(multi10inwords[multi10.index(x1)]+" "+first20inwords[first20.index(x2)])
    elif x in multi10:
        return(multi10inwords[multi10.index(x)])
    else:
        return(first20inwords[first20.index(x)])

sum = 0
for i in range(1,1001):
    string = WordNumber(i)
    string = string.lower()
    string = string.replace(" ","")
    sum += len(string)

print(sum)
