
# Simulate a simple guessing game where the program picks a random number and the user has to guess it.

import random
number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("Congratulations! You guessed it right.")