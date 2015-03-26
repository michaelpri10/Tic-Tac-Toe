from clearScreen import clearScreen

try:
    input=raw_input
except NameError:
    pass

def modeChoices():
    print("  1. Player vs Player")
    print("  2. Player vs Bot")
    print("  3. Bot vs Bot")

def chooseMode():
    modeChoices()
    gameMode = input("Which mode would you like to play? ")
    while gameMode not in ["1", "2", "3"]:
        clearScreen()
        print("Invalid Input")
        modeChoices()
        gameMode = input("Which mode would you like to play? ")
    if gameMode == "1":
        return "p1vsp2()"
    elif gameMode == "2":
        return "p1vsai()"
    elif gameMode == "3":
        return "aivsai()"
