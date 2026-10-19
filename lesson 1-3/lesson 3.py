number1 = int(input())
action = input()
number2 = int(input())

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