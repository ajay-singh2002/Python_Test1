# Print the factorial of a number using a loop.
num = int(input("enter the number = "))
fact = 1

for i in range(1, num+1):
    fact *= i
print("Factorial of", num, "is", fact)