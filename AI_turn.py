import random

# This will run if you selected EASY
def AI_turn_easy(board, possible_nums):

    # generates a random, available space on the board and makes it an 'O'
    randChoice = random.choice(possible_nums)
    possible_nums.remove(randChoice)
    board.spaces[randChoice] = "O"

    return possible_nums

# This will run if you selected HARD
def AI_turn_hard(board, possible_nums):

    # All of the possible winning configurations
    possible_configs = [["1", "2", "3"],
                        ["1", "4", "7"],
                        ["1", "5", "9"],
                        ["2", "5", "8"],
                        ["3", "6", "9"],
                        ["3", "5", "7"],
                        ["4", "5", "6"],
                        ["7", "8", "9"]]

    # Shuffles the configurations so the computer doesn't run through the same order every time
    random.shuffle(possible_configs)

    # Check each configuration; if there is two of the three spaces equal each other, put an 'O' in the other space
    for config in possible_configs:
        if board.spaces[config[0]] == board.spaces[config[1]]:
            if board.spaces[config[2]] in possible_nums:
                possible_nums.remove(board.spaces[config[2]])
                board.spaces[config[2]] = "O"
                return possible_nums
        elif board.spaces[config[0]] == board.spaces[config[2]]:
            if board.spaces[config[1]] in possible_nums:
                possible_nums.remove(board.spaces[config[1]])
                board.spaces[config[1]] = "O"
                return possible_nums
        elif board.spaces[config[1]] == board.spaces[config[2]]:
            if board.spaces[config[0]] in possible_nums:
                possible_nums.remove(board.spaces[config[0]])
                board.spaces[config[0]] = "O"
                return possible_nums
        else:
            pass

    # If there aren't any matches of two in any of the rows, choose a random, available space
    return AI_turn_easy(board, possible_nums)
