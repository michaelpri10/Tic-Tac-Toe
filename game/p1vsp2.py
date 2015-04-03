from board_class import Board
from user_turn import p1_turn, p2_turn
from check_win import check_win
from clearScreen import clearScreen
import time

def p1vsp2():
    clearScreen()

    board = Board()
    turns_taken = 0
    possible_nums = [str(i) for i in range (1,10)]
    print("Player 1 is 'O' and will go first")
    print("Player 2 is 'X' and will go second")
    time.sleep(2)
    p1_XO = "O"
    p2_XO = "X"
    last_move = "p2"

    while turns_taken < 9:
        clearScreen()
        board.print_board()

        if last_move == "p2":
            print("Player 1's Turn")
            possible_nums = p1_turn(board, possible_nums, p1_XO)
            last_move = "p1"
        elif last_move == "p1":
            print("Player 2's turn")
            possible_nums = p1_turn(board, possible_nums, p2_XO)
            last_move = "p2"

        win = check_win(board, turns_taken)
        if win == None:
            pass
        else:
            break

        turns_taken += 1

    clearScreen()
    board.print_board()

    if win == p1_XO:
        print("Player 1 wins! Congratulations :)")
        time.sleep(1.5)
    elif win == p2_XO:
        print("Player 2 wins! Congratulations :)")
        time.sleep(1.5)
    else:
        print("It was a draw")
        time.sleep(1.5)

    time.sleep(1.5)
