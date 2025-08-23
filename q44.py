# (Problem Solving) Write a program to generate the first 10 Fibonacci numbers.

a, b = 0, 1
print("Fibonacci Series:")

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b