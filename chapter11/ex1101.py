#print('ex11.01')

import re
fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'regex_sum_42.txt'
totalsum = list()
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    numb = re.findall('[0-9]+', line)
    if len(numb) < 1 : continue
    for nums in numb:
        intnum = int(nums)
        totalsum.append(intnum)
#print(totalsum)
print('Sum:', sum(totalsum))
