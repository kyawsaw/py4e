print('ex0905')
fname = input('Enter File Name: ')
if len(fname) < 1 :
    fname = 'mbox-short.txt'

school = dict()

fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    line = line.split()
    email = line[1]
    atpos = email.find("@")
    email = email[atpos+1:]
    school[email] = school.get(email, 0) + 1
print(school)
