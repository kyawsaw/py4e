#print('မင်္ဂလာပါ')
count = 0
total = 0
while True:
    str_val = input('Enter Number: ')
    if str_val == 'done':
        break
    try:
        float_val = float(str_val)
        #print(float_val)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + float_val
print(count, total, total/count)
