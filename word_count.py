import pprint
import operator

f = open('big.txt','r')

bigfile = f.read()

wc = {}

biglist = bigfile.split(' ')

print(len(biglist))

for word in biglist:
    if not word in wc:
        wc[word] = 0
    wc[word] += 1

sorted_x = sorted(wc.items(), key=operator.itemgetter(1))

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(sorted_x)


