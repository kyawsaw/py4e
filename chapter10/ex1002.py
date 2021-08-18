#print('1002')
fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
time = dict()

fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    for hours in words:
        hours = words[5]
        hour = hours[:2]
    time[hour] = time.get(hour, 0) + 1
#print(time)
tup = list()
for k, v in time.items():
    ntup = (k, v)
    tup.append(ntup)

tup = sorted(tup)

for k, v in tup:
    print(k, v)
