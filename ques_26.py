# Write a program to calculate the sum of numbers from 1 to 100
total = sum(range(1, 101))
print(total)

# for using for loop
for num in range(1, 101):
    total += num            # total = total + num

print("Sum of numbers from 1 to 100 is:", total)