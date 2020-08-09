from random import *

run = True

def dice_roll():
    dice = randint(1,6)
    print(dice)

while run == True:
    dice_roll()
    roll_again = input("Would you like to roll again")
    if roll_again == "yes":
        print("rolling again....")
    else:
        run = False
        