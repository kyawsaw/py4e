def computepay(hours, rate):
    #print("In computepay:", hours, rate)
    if hours > 40.0:
        reg_pay = hours * rate
        ot_pay = (hours - 40.0) * (rate * 0.5)
        pay = reg_pay + ot_pay
    else:
        pay = hours * rate
    #print("Returning pay", pay)
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
float_hour = float(hours)
float_rate = float(rate)

computedpay = computepay(float_hour, float_rate)
print("Pay: ", computedpay)
