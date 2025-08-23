# (Functions) Write a function that finds the second largest number in a list.
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

print(second_largest([10, 20, 4, 45, 99]))