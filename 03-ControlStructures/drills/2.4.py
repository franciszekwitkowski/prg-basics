number1 = input('Enter first number: ')
number2 = input('Enter second number: ')
operator = input('Enter operator (+, -, *, /): ')


if operator == '+':
        result = float(number1) + float(number2)
elif operator == '-':
        result = float(number1) - float(number2)
elif operator == '*':
        result = float(number1) * float(number2)
elif operator == '/':
        result = float(number1) / float(number2)
else:
        result = 'Invalid operator'

    # print result
print(f'{number1} {operator} {number2} = {result:g}')