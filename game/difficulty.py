from clearScreen import clearScreen
import time

try:
    input = raw_input
except NameError:
    pass

def difficultyChoice():
    print("  1.  FÁCIL")
    print("  2.  DIFÍCIL")
    print("  3.  IMPOSIBLE")

def difficulty():
    difficultyChoice()
    d_choice = input("¿Qué dificultades le gustaría? ")
    while d_choice.isdigit() == False or int(d_choice) not in [1,2,3]:
        clearScreen()
        print("Entrada no válida")
        difficultyChoice()
        d_choice = input("¿Qué dificultades le gustaría? ")
    if int(d_choice) in [1,2,3]:
        if int(d_choice) == 1:
            print("Has elegido FÁCIL")
            time.sleep(1.5)
            return "E"
        elif int(d_choice) == 2:
            print("Has elegido DIFÍCIL")
            time.sleep(1.5)
            return "H"
        elif int(d_choice) == 3:
            print("Has elegido IMPOSIBLE")
            time.sleep(1.5)
            return "I"
