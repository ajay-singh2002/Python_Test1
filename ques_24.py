# Print a right-angled triangle of stars using nested loops
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()