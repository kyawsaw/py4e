#print('11.00')

import re
fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)
numlist = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
