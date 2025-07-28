# Generate a number pyramid (1, 22, 333, ...).

rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    print(str(i) * (2*i - 1))