# (Functions) Write a function that takes two numbers and returns both their sum and difference.
def sum_and_difference():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2, num1 - num2

# Function call
total, diff = sum_and_difference()
print("Sum = ", total)
print("Difference = ", diff)