def list (numbers):
    first = []
    zeros = []

    for number in numbers :
        if number != 0:
            first.append(number)
        else:
            zeros.append(number)
    return first + zeros






