import random

print("...rock...")
print("...paper...")
print("...scissors...")

choices = ['rock', 'paper', 'scissors']

player_1_choice = input("Enter your choice: ")
player_1 = player_1_choice.lower()

player_2 = random.choice(choices)

if player_1 in choices and player_2 in choices:
    print("Your choice was: " + player_1)
    print("Computers choice was: " + player_2)
    print("****")
    if player_1 == player_2:
        print('draw')
    if player_1 == 'rock':
        if player_2 == 'paper':
            print('player 2 wins')
        if player_2 == 'scissors':
            print('player 1 wins')
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('player 1 wins')
        if player_2 == 'scissors':
            print('player 2 wins')
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print('player 2 wins')
        if player_2 == 'paper':
            print('player 1 wins')
    else:
        print('solution not provided')
else:
    print('Please provide a valid input')