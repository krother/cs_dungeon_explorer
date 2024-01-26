"""
Guess the Number game:

1. The program randomly 'rolls' a number between 1 and 100.
2. The player enters a number
3. The program says whether the number was too big or too small.
4. Repeat steps 3-5 until the correct number was guessed.
"""
from random import randint

def guess_game():
    number = randint(a=1, b=100)
    x=0
    while(x!=number):
        x=int(input('Enter the number between 1 n 100: '))
        if x > number:
            print('Number is too big')
        elif(x<number):
            print('Number is too small')
        else:
            print('Number is found')


if __name__ == "__main__":
    guess_game()
