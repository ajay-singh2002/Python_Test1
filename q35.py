# (Functions with Loops) Write a function that takes a list of numbers and returns the maximum.
def find_max(numbers):

    maximum = numbers[0]


    for num in numbers:
        if num > maximum:
            maximum = num  

    return maximum


# Example
nums = [10, 25, 7, 89, 42]
print(find_max(nums))