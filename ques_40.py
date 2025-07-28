# Write a code to print a hollow square pattern with diagonals.
n = 5  # square size

for i in range(n):
    for j in range(n):
        # Border OR Diagonal पर star print करो
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()