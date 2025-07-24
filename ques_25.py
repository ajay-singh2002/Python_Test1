# Print a multiplication table from 1 to 5 using nested loops
for i in range(1, 6):           # Rows → 1 to 5
    for j in range(1, 6):       # Columns → 1 to 5
        print(f"{i*j:2}", end=" ")  # Print product
    print()