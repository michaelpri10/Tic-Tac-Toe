# Helps with compatibilty for Python 3.x
try:
    input = raw_input
except NameError:
    pass

# Runs when it is the user's turn
def p1_turn(board, possible_nums):
    print("Player 1's turn")

    # If the input by the user is valid (1-9) and not taken yet, mark the spot with and 'X'
    choice = input("Choose a space on the board (1-9) ")
    while choice.isdigit() == False or int(choice) not in range(1,10) or choice not in possible_nums:
        print("Invalid Input")
        choice = input("Choose a space on the board (1-9) ")
    if int(choice) in range(1,10):
        possible_nums.remove(choice)
        board.spaces[choice] = "X"

    return possible_nums
    



        
        
