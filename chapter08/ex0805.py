fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file:', fname)
    quit()
count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1]
    count += 1
    print(line)
print('There were', count, 'lines in the file with From as the first word')
