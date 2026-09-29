def task_1():
    numbers = [1,2,3,4,5,6]
    numbers[:len(numbers) // 2 ]
    numbers[len(numbers) // 2:]
    print(numbers[:len(numbers) // 2], numbers[len(numbers) // 2:])

def task_2():
    numbers = [1,2,3]
    [numbers[:2]]
    [numbers[2:]]
    print ([numbers [:2], numbers[2:]])

def task_3():
    numbers = [1,2,3,4,5]
    print((len(numbers) + 1) // 2)
    print([numbers[:3], numbers[3:]])

def task_4():
    numbers = [1]
    [numbers[:1]]
    [numbers[1:]]
    print([numbers[:1], numbers[1:]])

def task_5():
    numbers = []
    [numbers [:1]]
    print([numbers[:1], numbers[1:]])
