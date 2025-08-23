# (Loops) Find the largest number in a list using a loop
numbers = [12, 45, 67, 23, 89, 34]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print("Largest number is:", largest)


