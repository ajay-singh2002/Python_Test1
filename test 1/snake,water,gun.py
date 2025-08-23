import random

computer = random.choice(['snake', 'water', 'gun'])
user = input("Choose snake, water or gun: ")

if user == computer:
    print("Tie! Both chose", user)
elif user == 'snake' and computer == 'water':
    print("You win! Snake drinks water")
elif user == 'water' and computer == 'gun':
    print("You win! Water damages gun")
elif user == 'gun' and computer == 'snake':
    print("You win! Gun kills snake")
elif user == 'snake' and computer == 'gun':
    print("You lose! Gun kills snake")
elif user == 'water' and computer == 'snake':
    print("You lose! Snake drinks water")
elif user == 'gun' and computer == 'water':
    print("You lose! Water damages gun")
else:
    print("Invalid input")
