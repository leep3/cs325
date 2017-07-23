import random

output = open('./data.txt', 'w')

list = []
for x in range (0, 100):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 250):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 500):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 750):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 1000):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 1500):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))

list = []
for x in range (0, 2000):
    list.append(random.randint(-1000, 1000))
output.write(" ".join(map(lambda x: str(x), list)))
output.write("\n")
print("generated:", len(list))
