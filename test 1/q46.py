# Given a list of numbers, create a dictionary with numbers as keys and their squares as values.
def squares_dict(numbers):
    result = {}
    for num in numbers:
        result[num] = num ** 2
    return result

print(squares_dict([1, 2, 3, 4]))