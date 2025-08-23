# (Functions with Loops) Write a function that takes a list of numbers and returns their average.

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(average([2, 5, 8, 10]))