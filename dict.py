import random

list = []

for i in range(2,110,2):
    list.append(i)

print(len(list))
print(random.shuffle(list))

print(list)
