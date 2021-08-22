import re
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'mbox.txt'
fhand = open(fname)

form = '^N.+: ([0-9]+)'

totalnumb = list()
for line in fhand:
    matchs = re.findall((form), line)
    for match in matchs:
        numb = int(match)
        totalnumb.append(numb)
avarge = sum(totalnumb) / len(totalnumb)
print(int(avarge))
