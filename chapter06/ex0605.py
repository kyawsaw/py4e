#print('chpater06_ex05')
data = 'X-DSPAM-Confidence:0.8475'
fcpos = data.find(':')
#print(dotpos)
str_number = data[fcpos+1:]
#print(str_number)
float_number = float(str_number)
print(float_number)
