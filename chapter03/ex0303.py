score = input("Enter Score: ")
try:
    float_score = float(score)
except:
    print("Error, please enter numeric input")
    quit()
if float_score <= 0.0 or float_score >= 1.0:
    print("Please enter between 0.0 and 1.0 using decimal number")
elif float_score >= 0.9:
    print("A")
elif float_score >= 0.8:
    print("B")
elif float_score >= 0.7:
    print("C")
elif float_score >= 0.6:
    print("D")
elif float_score < 0.6:
    print("F")
