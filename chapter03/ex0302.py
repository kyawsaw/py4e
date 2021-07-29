str_hour = input("Enter Hours: ")
str_rate = input("Enter Rate: ")
# try & expect
try:
    float_hour = float(str_hour)
    float_rate = float(str_rate)
except:
    print("Error, please enter numeric input")
    quit() # program stop here
# print(float_hour, float_rate)
if float_hour > 40.0:
    # print("Overtime")
    reg_pay = float_hour * float_rate
    ot_pay = (float_hour - 40.0) * (float_rate * 0.5)
    pay = reg_pay + ot_pay
else:
    # print("Regular")
    pay = float_hour * float_rate
print("Pay: ", pay)
