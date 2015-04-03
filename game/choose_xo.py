from clearScreen import clearScreen

import time

try:
    input=raw_input
except NameError:
    pass

def chooseXO():
    choice = input("¿Quieres ser 'X' o 'O'? ('O' va primero) ")
    while choice.lower() not in ['x', 'o']:
        clearScreen()
        print("Entrada no válida")
        choice = input("¿Quieres ser 'X' o 'O'? ('O' va primero) ")
    if choice.lower() == 'x':
        print("Robot irá primero")
        time.sleep(1.5)
        return("p1", "O", "X")
    elif choice.lower() == 'o':
        print("Irás primero")
        time.sleep(1.5)
        return("AI", "X", "O")
