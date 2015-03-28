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
    print("Bot 1 is 'O' and will go first")
    print("Bot 2 is 'X' and will go second")
    time.sleep(2)
    AI1_XO = "O"
    AI2_XO = "X"
    last_move = "AI2"

    AI1_moves = [AI_turn_easy, AI_turn_hard, AI_turn_impossible]
    AI2_moves = [AI_turn_easy, AI_turn_hard, AI_turn_impossible]

    while turns_taken < 9:
        clearScreen()
        board.print_board()

        if last_move == "AI2":
            print("Bot 1's Turn")
            time.sleep(1.5)
            possible_nums = random.choice(AI1_moves)(board, possible_nums, AI1_XO, AI2_XO)
            last_move = "AI1"
        elif last_move == "AI1":
            print("Bot 2's turn")
            time.sleep(1.5)
            possible_nums = random.choice(AI2_moves)(board, possible_nums, AI2_XO, AI1_XO)
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
        print("Bot 1 wins!")
        time.sleep(1.5)
    elif win == AI2_XO:
        print("Bot 2 wins!")
        time.sleep(1.5)
    else:
        print("It was a draw")
        time.sleep(1.5)

    time.sleep(1.5)
