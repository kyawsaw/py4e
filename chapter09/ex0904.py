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
# most sent address and count
most = None
count = None
for key, val in rec.items():
    if count is None or val > count :
        count = val
        most = key
print(most, count)
