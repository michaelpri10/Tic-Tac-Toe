from clearScreen import clearScreen

try:
    input=raw_input
except NameError:
    pass

def modeChoices():
    print("  1. Player vs Player")
    print("  2. Player vs Bot")

def chooseMode():
    modeChoices()
    gameMode = input("Which mode would you like to play? ")
    while gameMode not in ["1", "2"]:
        clearScreen()
        print("Invalid Input")
        modeChoices()
        gameMode = input("Which mode would you like to play? ")
    if gameMode == "1":
        return "p1vsp2()"
    else:
        return "p1vsai()"
