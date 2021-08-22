import re
fname = 'mbox.txt'

fhand = open(fname)
tofind = input('Enter a regular expression: ')

count = 0
for line in fhand:
    #line = line.rstrip()
    matchs = re.findall((tofind), line)
    #print(matchs)
    if len(matchs) < 1 : continue
    for match in matchs:
        count +=1
        #print(matchs)
print(fname, 'had', count,'lines that matched', tofind)
