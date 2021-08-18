fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'clown.txt'

count = dict()
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    line = line.lower()
    words = line.split()
    for word in words:
        for char in word:
            if char.isalpha():
                count[char] = count.get(char, 0) + 1
#print(count)
temp = list()
for k, v in count.items():
    ntuple = (v, k)
    temp.append(ntuple)

temp = sorted(temp, reverse=True)

for k, v in temp:
    print(v, k)
