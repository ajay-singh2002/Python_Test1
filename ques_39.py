# Create a program to generate a prime number pyramid
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

rows = int(input("Enter rows: "))
num = 2

for i in range(1, rows + 1):
    print("  " * (rows - i), end="")
    count = 0
    while count < i:
        if is_prime(num):
            print(f"{num:2d} ", end=" ")
            count += 1
        num += 1
    print()



