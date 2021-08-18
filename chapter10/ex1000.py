fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
#dictionary part
dic = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for word in words:
        # idoms: retrive/create/update
        dic[word] = dic.get(word, 0) + 1
#print(dic)

temp = list()
for k, v in dic.items():
    ntuple = (v, k)
    temp.append(ntuple)
#print('Flipped ', temp)

temp = sorted(temp, reverse=True)
#print('Sorted ', temp)

for v, k in temp[:5]:
    print(k, v)
