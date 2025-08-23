# import random
#
# computer = random.choice(['stone', 'paper', 'scissor'])
# user = input("enter stone, paper, scissor ")
#
# if user == computer:
#     print("tie both choose", user)
# elif user == 'stone' and computer == 'scissor':
#     print("you win because (stone break scissor)")
# elif user == 'paper' and computer == 'stone':
#     print("you win because (paper wrap stone)")
# elif user == 'scissor' and computer == 'paper':
#     print("you win because (scissor cut paper)")
# elif user == 'stone' and computer == 'paper':
#     print("you lose because (paper wrap stone)")
# elif user == 'scissor' and computer == 'stone':
#     print("you lose because (stone break scissor)")
# elif user == 'paper'and computer == 'scissor':
#     print("you lose because (scissor cut paper  )")
# else:
#     print("invalid input, user")

num = 1
while num <= 10:
    if num %2 !=0:
        print(num)
    num += 1