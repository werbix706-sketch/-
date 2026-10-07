while True:
    number1 = int(input('Enter first number: '))
    action = input('Enter action: ')
    number2 = int(input('Enter second number: '))

    if action == '+':
        result = number1 + number2
        print(result)

    if action == '-':
        result = number1 - number2
        print(result)

    if action == '*':
        result = number1 * number2
        print(result)

    if action == '/':
        if number2 != 0:
            result = number1 / number2
            print(result)
    answer = input('Continue? (y/n): ')
    if answer !='y':
        break

