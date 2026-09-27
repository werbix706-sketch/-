def task_1():
    number = int(input( ))
    print( number  ** 2)

def task_2():
    number1, number2, number3 = input().split(",")
    number1 = int( number1 )
    number2 = int( number2 )
    number3 = int( number3 )
    average = (number1 + number2 + number3) / 3
    print( average )

def task_3():
    minutes = int(input())
    hours = minutes // 60
    remaining = minutes % 60
    print(hours, "hours", remaining, " minutes")

def task_4():
    price = int(input() or 0)
    sale = int(input() or 0)
    discount = price * sale / 100
    final = price - discount
    print(final)

def task_5():
    number = int(input())
    print(number % 10)

def task_6():
    length = int(input())
    width = int(input())
    perimeter = 2 * (length + width)
    print(perimeter)

def task_7():
    number = int(input())
    print(number // 1000)
    print((number // 100) % 10)
    print((number // 10) % 10)
    print(number % 10)







