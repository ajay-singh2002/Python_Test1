# (Functions with Loops) Write a function that takes a list and returns a new list with only even
# numbers

def even_list(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list


print(even_list([22, 32, 55, 56, 24, 21, 26, 84]))
