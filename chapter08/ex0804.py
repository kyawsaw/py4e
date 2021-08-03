#input file to open
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

wlist = list()
for line in fhand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in wlist: continue
        else:
            wlist.append(word)
            wlist.sort()
print(wlist)
