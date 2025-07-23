# Ask a user for age and print if they are a child, teen, or adult.
age = int(input("enter your age = "))
if age <= 10:
    print("you are child")

elif age < 18:
    print("you are teen")

elif age >= 18:
    print("you are adult")