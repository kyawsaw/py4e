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
    line = line.rstrip()    #strip \n aka newline
    if not line.startswith('X-DSPAM-Confidence:'):  #if newline not startswith given string
        continue                                    #then skip the line & move on
    #space = line.find('X-DSPAM-Confidence:')
    #print(space)
    extract = line[20:]
    #print('Extracted', extract)
    fextract = float(extract)
    #print('Extracted', fextract)
    total = total + float(extract)
    count = count + 1
print('Average spam confidence:', total/count)
#print(count, total, total/count)
