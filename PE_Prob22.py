f = open("/home/fractaluser/Documents/p022_names.txt", "r")

data = f.read().replace("'", "")

data = data.split(",")

f.close()

print(data[:10])
