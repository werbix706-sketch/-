numbers = [10,5,2,8]
if len(numbers) <= 1:
    print(numbers)
else:
    [numbers[-1]] + numbers[:-1]
print([numbers[-1]] + numbers[:-1])