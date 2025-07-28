# Print a diamond pattern using loops.
rows = 5

# Upper Pyramid
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Lower Pyramid
for i in range(rows-1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)