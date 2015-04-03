from clearScreen import clearScreen

try:
    input = raw_input
except NameError:
    pass

def p1_turn(board, possible_nums, p1_XO):
    choice = input("Elija un espacio en el tablero (1-9) ")
    while choice.isdigit() == False or int(choice) not in range(1,10) or choice not in possible_nums:
        clearScreen()
        board.print_board()
        print("Entrada no válida")
        choice = input("Elija un espacio en el tablero (1-9) ")
    if int(choice) in range(1,10):
        possible_nums.remove(choice)
        board.spaces[choice] = p1_XO

    return possible_nums

def p2_turn(board, possible_nums, p2_XO):
    choice = input("Elija un espacio en el tablero (1-9) ")
    while choice.isdigit() == False or int(choice) not in range(1,10) or choice not in possible_nums:
        clearScreen()
        print("Entrada no válida")
        choice = input("Elija un espacio en el tablero (1-9) ")
    if int(choice) in range(1,10):
        possible_nums.remove(choice)
        board.spaces[choice] = p2_XO

    return possible_nums
