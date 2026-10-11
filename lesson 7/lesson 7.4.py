def common_elements():
    threes = (number for number in range(100) if number % 3 == 0)
    fives = (number for number in range(100) if number % 5 == 0)
    return set(threes).intersection(set(fives))
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}





