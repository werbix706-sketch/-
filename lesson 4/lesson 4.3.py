import random
from unittest import result

length = random.randint(3,10)
numbers = []
for i in range(length):
    numbers.append(random.randint(1,10))

result = []
result.append(numbers[0])
result.append(numbers[2])
result.append(numbers[-2])

print(numbers)
print(result)
