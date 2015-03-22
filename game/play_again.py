from clearScreen import clearScreen

try:
    input = raw_input
except NameError:
    pass

def play_again():
    p_a_choice = str(input("Play again? (y or n) ")).lower()
    while p_a_choice not in ["y", "n"]:
        clearScreen()
        print("Invalid Input")
        p_a_choice = str(input("Play again? (y or n) ")).lower()
    if p_a_choice == 'n':
        print("Goodbye")
        clearScreen()
        return False
    elif p_a_choice == 'y':
        return True
