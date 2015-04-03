from board_class import Board
from ai_turn import AI_turn_easy, AI_turn_hard, AI_turn_impossible
from check_win import check_win
from clearScreen import clearScreen
import time
import random

def aivsai():
    clearScreen()

    board = Board()
    turns_taken = 0
    possible_nums = [str(i) for i in range (1,10)]
    print("Robot 1 es 'O' y vayan en primer lugar")
    print("Robot 2 es 'X' y vayan en segundo lugar")
    time.sleep(2)
    AI1_XO = "O"
    AI2_XO = "X"
    last_move = "AI2"

    AI1_moves = ["AI_turn_easy(board, possible_nums, AI1_XO)", "AI_turn_hard(board, possible_nums, AI1_XO, AI2_XO)", "AI_turn_impossible(board, possible_nums, AI1_XO, AI2_XO)"]
    AI2_moves = ["AI_turn_easy(board, possible_nums, AI2_XO)", "AI_turn_hard(board, possible_nums, AI2_XO, AI1_XO)", "AI_turn_impossible(board, possible_nums, AI2_XO, AI1_XO)"]

    while turns_taken < 9:
        clearScreen()
        board.print_board()

        if last_move == "AI2":
            print("Robot 1 turno")
            time.sleep(1.5)
            possible_nums = eval(random.choice(AI1_moves))
            last_move = "AI1"
        elif last_move == "AI1":
            print("Robot 2 turno")
            time.sleep(1.5)
            possible_nums = eval(random.choice(AI2_moves))
            last_move = "AI2"

        win = check_win(board, turns_taken)
        if win == None:
            pass
        else:
            break

        turns_taken += 1

    clearScreen()
    board.print_board()

    if win == AI1_XO:
        print("Robot 1 gana!")
        time.sleep(1.5)
    elif win == AI2_XO:
        print("Robot 2 gana!")
        time.sleep(1.5)
    else:
        print("Era un empate")
        time.sleep(1.5)

    time.sleep(1.5)
