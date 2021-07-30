def computegrade(score):
    #print("computing grade")
    if score <= 0.0 or score >= 1.0:
        return "Please enter between 0.0 and 1.0"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"

score = input("Enter Score: ")
try:
    float_score = float(score)
except:
    print("Error, please enter numeric input")
    quit()

computedgrade = computegrade(float_score)
print(computedgrade)
