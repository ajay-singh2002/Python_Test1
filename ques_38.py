# Check if a given number is an Armstrong number.
num = int(input("Enter a number: "))
power = len(str(num))

sum_digits = sum(int(d)**power for d in str(num))

if sum_digits == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")
