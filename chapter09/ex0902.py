#print('exercise0902')
fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
dic = dict()
for line in hand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    for day in words:
        day = words[2]
    dic[day] = dic.get(day, 0) + 1
print(dic)
