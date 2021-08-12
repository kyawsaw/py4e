#print('0903')
fname = input('Enter File Name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
rec = dict()
for line in hand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    addr = line.split()
    #print(addr)
    for mail in addr:
        mail = addr[1]
    #print(mail)
    rec[mail] = rec.get(mail, 0) + 1
print(rec)
