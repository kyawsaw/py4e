fname = open('mbox-short.txt')

for line in fname:
    sline = line.rstrip()
    print(sline)
