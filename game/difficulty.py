from clearScreen import clearScreen
import time

try:
    input = raw_input
except NameError:
    pass

def difficultyChoice():
    print("  1.  EASY")
    print("  2.  HARD")
    print("  3.  IMPOSSIBLE")

def difficulty():
    difficultyChoice()
    d_choice = input("What difficulty would like? ")
    while d_choice.isdigit() == False or int(d_choice) not in [1,2,3]:
        clearScreen()
        print("Invalid Input")
        difficultyChoice()
        d_choice = input("What difficulty would like? ")
    if int(d_choice) in [1,2,3]:
        if int(d_choice) == 1:
            print("You have chosen EASY")
            time.sleep(1.5)
            return "E"
        elif int(d_choice) == 2:
            print("You have chosen HARD")
            time.sleep(1.5)
            return "H"
        elif int(d_choice) == 3:
            print("You have chosen IMPOSSIBLE")
            time.sleep(1.5)
            return "I"
