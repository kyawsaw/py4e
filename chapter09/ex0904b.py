#print('ex0904b')
#extract emial address (list)
fname = 'mbox-short.txt'
hand = open(fname)
emails_list = list()
for line in hand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    line = line.split()
    emails = line[1]
    emails_list.append(emails)
#print(emails_list)
#creat histogram (dict)
histogram = dict()
for email in emails_list:
    histogram[email] = histogram.get(email, 0) + 1
#print(histogram)
#count and find most sent email address
most = None
count = None
for key, val in histogram.items():
    if count is None or val > count :
        count = val
        most = key
print(most, count)
