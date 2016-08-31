import random



# States = ['Texas','Oklahoma']
# Capitals = ['Austin','OKC']

# for i in range(len(States)):
#     print(States[i],Capitals[i])

capitals = {
    'Texas':'Austin',
    'Oklahoma':'Okc',
    'Delaware':'Dover',
    'California':'Sacramento',
    'Alabama':'Montgomery',
    'Alaska':'Juneau',
    'Nebraska':'Lincoln',
    'Arizona':'Phoenix',
    'Nevada':'Carson City'
}

""" Iterate over keys """

for x in capitals:
    print(x)
    # prints Alabama \n Alaska \n Nebraska, ...

""" Iterate over (key, value) tuples """

for key, value in capitals.items():
    print(key,value)
    # prints Alabama,Montgomery \n Alaska,Juneau \n ...

""" Iterate over values """

for value in capitals.values():
    print(value)
    # prints Montgomery \n Juneau \n ...

""" Check for existence of key """

if 'Nevada' in capitals:
    print('the key Nevada exists')


# L = []

# L.append(3.14159)
# L.append("bananas")
# L.append("your momma")

# for i in range(34):
#     L.append(random.randint(1,10))

# L.insert(len(L),["donkey",9])
# print(len(L))
# L.remove(5)

# print(len(L))




# list = []

# for i in range(2,110,2):
#     list.append(i)

# print(len(list))
# print(random.shuffle(list))

# print(list[4:8])

