from clearScreen import clearScreen

try:
    input=raw_input
except NameError:
    pass

def modeChoices():
    print("  1. Jugador contra Jugador")
    print("  2. Jugador contra Robot")
    print("  3. Robot contra Robot")

def chooseMode():
    modeChoices()
    gameMode = input("¿Modo en que te gustaría jugar? ")
    while gameMode not in ["1", "2", "3"]:
        clearScreen()
        print("Entrada no válida")
        modeChoices()
        gameMode = input("¿Modo en que te gustaría jugar? ")
    if gameMode == "1":
        return "p1vsp2()"
    elif gameMode == "2":
        return "p1vsai()"
    elif gameMode == "3":
        return "aivsai()"
