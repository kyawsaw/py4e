#print('chapter09')
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
# most common word and count
largest = -1
theword = None
for key, value in dic.items():
    print(key, value)
    if value > largest:
        largest = value
        theword = key
print('Common word', theword, 'Appeared', largest, 'times')
