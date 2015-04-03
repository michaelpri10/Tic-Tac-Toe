from board_class import Board
from difficulty import difficulty
from choose_xo import chooseXO
from ai_turn import AI_turn_easy, AI_turn_hard, AI_turn_impossible
from user_turn import p1_turn
from check_win import check_win
from play_again import play_again
from clearScreen import clearScreen
from chooseMode import chooseMode
from p1vsai import p1vsai
from p1vsp2 import p1vsp2
from aivsai import aivsai
import time

def main():
    clearScreen()
    game_mode = chooseMode()
    eval(game_mode)

    times_played = 0
    while times_played < 10:
        clearScreen()
        if play_again():
            game_mode = chooseMode()
            eval(game_mode)
            times_played += 1
        else:
            break

    print("Adiós")
    time.sleep(1.5)
    quit()

if __name__ == "__main__":
    main()
