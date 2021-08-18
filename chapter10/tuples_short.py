#print('10.0')
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)

lst = list()
lst = sorted([(val, key) for key, val in counts.items()], reverse=True)
#print(lst)

for val, key in lst[:10]:
    print(key, val)
