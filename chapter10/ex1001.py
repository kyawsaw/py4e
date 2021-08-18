#print('1001')
fname = input('Enter File Name: ')
if len(fname) < 1 :
    fname = 'mbox-short.txt'
email = dict()
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    addr = line.split()
    for who in addr:
        who = addr[1]
    email[who] = email.get(who, 0) + 1
#print(email)
tup = list()
for k, v in email.items():
    ntuple = (v, k)
    tup.append(ntuple)

tup = sorted(tup, reverse=True)

for v, k in tup[:1]:
    print(k, v)
