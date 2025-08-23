# (Problem Solving) Write a program to check if a number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a Prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is NOT a Prime number")