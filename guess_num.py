# Project number 2
from random import *

global points
points = 10
global x
x = True

mystery_num = randint(1,10)
while x == True:
    guess = int(input('Enter your number between 1 and 10'))
    if guess == mystery_num:
        print("You guessed correctly")
        print(points)
        x = False
    elif guess > mystery_num:
        print("You guess is greater than the number")
        points -= 1
    elif guess < mystery_num:
        print("The mystery number is greater than your guess")
        points -= 1
    
        

