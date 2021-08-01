#input file to open
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

#count
count = 0
total = 0
for line in fhand:
    line = line.rstrip()    
    if line.startswith('X-DSPAM-Confidence:'):
        extract = line[20:]
        fextract = float(extract)
        total = total + float(extract)
        count = count + 1
print('Average spam confidence:', total/count)
#print(count, total, total/count)
