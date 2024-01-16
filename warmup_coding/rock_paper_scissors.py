"""
A rock-paper-scissors game
"""
import random

player = input("Please enter R, P or S (for [R]ock, [P]aper and [S]cissors) ")
computer = random.choice('RPS')

if player == 'R':
    if computer == 'P':
        print(f'Computer: {computer}, computer wins')
    elif computer == 'S':
        print(f'Computer: {computer}, Player wins')
    else:
        print(f'Computer: {computer}, It is a draw!')
elif player == 'P':
    if computer == 'P':
        print(f'Computer: {computer}, It is a draw!')
    elif computer == 'S':
        print(f'Computer: {computer}, computer wins')
    else:
        print(f'Computer: {computer}. Player wins')
else:
    if computer == 'P':
        print(f'Computer: {computer}, Player wins')
    elif computer == 'S':
        print(f'Computer: {computer}, draw')
    else:
        print(f'Computer: {computer}. computer wins')


