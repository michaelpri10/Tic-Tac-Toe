from clearScreen import clearScreen

import time

try:
    input=raw_input
except NameError:
    pass

def chooseXO():
    choice = input("Would you like to be 'X' or 'O'? ('O' goes first) ")
    while choice.lower() not in ['x', 'o']:
        clearScreen()
        print("Invalid Input")
        choice = input("Would you like to be 'X' or 'O'? ('O' goes first) ")
    if choice.lower() == 'x':
        print("Bot will go first")
        time.sleep(1.5)
        return("p1", "O", "X")
    elif choice.lower() == 'o':
        print("You will go first")
        time.sleep(1.5)
        return("AI", "X", "O")
