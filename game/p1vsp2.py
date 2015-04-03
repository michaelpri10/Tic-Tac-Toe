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
    print("Jugador 1 es 'O' y vayan en primer lugar")
    print("Jugador 2 es 'X' y vayan en segundo lugar")
    time.sleep(2)
    p1_XO = "O"
    p2_XO = "X"
    last_move = "p2"

    while turns_taken < 9:
        clearScreen()
        board.print_board()

        if last_move == "p2":
            print("Jugador 1 turno")
            possible_nums = p1_turn(board, possible_nums, p1_XO)
            last_move = "p1"
        elif last_move == "p1":
            print("Jugador 2 turno")
            possible_nums = p2_turn(board, possible_nums, p2_XO)
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
        print("Jugador 1 gana! Felicitaciones :)")
        time.sleep(1.5)
    elif win == p2_XO:
        print("Jugador 2 gana! Felicitaciones :)")
        time.sleep(1.5)
    else:
        print("Era un empate")
        time.sleep(1.5)

    time.sleep(1.5)
