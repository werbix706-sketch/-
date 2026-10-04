def list(numbers):
    if not numbers:
        return 0
    summa = 0
    for i in range(0, len(numbers), 2):
        summa += numbers[i]
    return summa * numbers[-1]


