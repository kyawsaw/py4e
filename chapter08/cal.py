number1 = int(input('Enter number: '))
number2 = int(input('Enter number: '))
operator = input('Enter operator: ')

if operator == '+' :
    result = number1 + number2
    print('number1 + number2 is',result)

elif operator == '-' :
    result = number1 - number2
    print('number1 - number2 is',result)

elif operator == '*' :
    result = number1 * number2
    print('number1 * number2 is',result)

elif operator == '/' :
    result = number1 / number2
    print('number1 / number2 is',result)
