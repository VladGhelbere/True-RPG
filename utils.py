import random
import os

def throw_dice():
    dice1 = random.randint(1,10)
    dice2 = random.randint(1,10)
    dice3 = random.randint(1,10)
    return [dice1, dice2, dice3]

def press_any_key():
    open = True
    while (open):
        input("Press any key to continue...")
        cls()
        break

def cls():
    os.system('cls' if os.name=='nt' else 'clear')