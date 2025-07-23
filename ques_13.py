# Create a nested condition to check if a number is positive and even
number = int(input("enter a number = "))

if number > 0:              # Pehle Positive check
    if number % 2 == 0:     # Positive hone ke baad Even check
        print("Positive and Even")
    else:
        print("Positive but Odd")
else:
    print("Not Positive")