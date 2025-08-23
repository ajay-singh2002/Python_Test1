# (Functions with Loops) Write a function that reverses a list without using reverse()

def reverse_list(lst):
    new_list = []
    for item in lst:
        new_list = [item] + new_list
    return new_list

print(reverse_list([1, 2, 3, 4]))