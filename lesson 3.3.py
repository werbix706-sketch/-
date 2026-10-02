def split_list(numbers):
    split = (len(numbers) + 1) // 2
    first = numbers[:split]
    second = numbers[split:]
    return [first, second]
