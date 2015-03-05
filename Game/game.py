from board_class import Board
from difficulty import difficulty
from chooseXO import chooseXO
from AI_turn import AI_turn_easy, AI_turn_hard
from user_turn import p1_turn
from check_win import check_win
from play_again import play_again
import time

def main():
    def tic_tac_toe():
        # print("\n" * n) - makes it appear as if it is a new screen

        print("\n" * 500)
        
        diff = difficulty()
        time.sleep(2)
        
        board = Board()
        turns_taken = 0
        possible_nums = [str(i) for i in range (1,10)]
        last_move = chooseXO()

        while turns_taken < 9:
            print("\n" * 200)
            board.print_board()

            if last_move == "p1":
                print("AI's turn")
                time.sleep(1.5)
                if diff == "E":
                    possible_nums = AI_turn_easy(board, possible_nums)
                elif diff == "H":
                    possible_nums = AI_turn_hard(board, possible_nums)
                last_move = "AI"
                
            elif last_move == "AI":
                possible_nums = p1_turn(board, possible_nums)
                last_move = "p1"

            win = check_win(board, turns_taken)
            if win == None:
                pass
            else:
                break
            
            turns_taken += 1

        print("\n" * 200)
        board.print_board()

        if win == "O":
            print("AI wins. You lose :(")
        elif win == "X":
            print("You win :). Congratulations!")
        elif win == "draw":
            print("It was a draw")

        time.sleep(2)

    tic_tac_toe()

    times_played = 1
    while times_played < 10:
        print("\n" * 200)
        if play_again():
            tic_tac_toe()
            times_played += 1
        else:
            break

    quit()

if __name__ == "__main__":
    main()
    

        
