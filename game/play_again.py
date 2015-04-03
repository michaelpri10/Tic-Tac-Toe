from clearScreen import clearScreen

try:
    input = raw_input
except NameError:
    pass

def play_again():
    p_a_choice = str(input("¿Jugar otra vez? (s or n) ")).lower()
    while p_a_choice not in ["s", "n"]:
        clearScreen()
        print("Entrada no válida")
        p_a_choice = str(input("¿Jugar otra vez? (s or n) ")).lower()
    if p_a_choice == 'n':
        clearScreen()
        return False
    elif p_a_choice == 's':
        clearScreen()
        return True
