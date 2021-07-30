largest = None
smallest = None
while True:
    str_val = input('Enter Number: ')
    if str_val == 'done':
        break
    try:
        float_val = int(str_val) #float output show Mismatch on autograder
        #print(float_val)
    except:
        print('Invalid input')
        continue
    if largest is None or float_val > largest :
        largest = float_val
    if smallest is None or float_val < smallest :
        smallest = float_val
print('Maximum ',largest)
print('Minimum ',smallest)
