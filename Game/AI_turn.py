import random

def AI_turn_easy(board, possible_nums, AI_XO):

    # generates a random, available space on the board and makes it an 'O'
    randChoice = random.choice(possible_nums)
    possible_nums.remove(randChoice)
    board.spaces[randChoice] = AI_XO

    return possible_nums

def avoid_losing_and_win_if_possible(board, possible_nums, AI_XO):

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
                board.spaces[config[2]] = AI_XO
                return possible_nums
        elif board.spaces[config[0]] == board.spaces[config[2]]:
            if board.spaces[config[1]] in possible_nums:
                possible_nums.remove(board.spaces[config[1]])
                board.spaces[config[1]] = AI_XO
                return possible_nums
        elif board.spaces[config[1]] == board.spaces[config[2]]:
            if board.spaces[config[0]] in possible_nums:
                possible_nums.remove(board.spaces[config[0]])
                board.spaces[config[0]] = AI_XO
                return possible_nums
        else:
            pass
    return None

def AI_turn_hard(board, possible_nums, AI_XO):

    move = avoid_losing_and_win_if_possible(board, possible_nums, AI_XO)

    if move != None:
        return move
    else:
        return AI_turn_easy(board, possible_nums, AI_XO)


def AI_turn_impossible(board, possible_nums, AI_XO):

    move = avoid_losing_and_win_if_possible(board, possible_nums, AI_XO)

    if move:
        return move
    else:
        c_m = ['5', '1', '7', '3', '9']
        random.shuffle(c_m)
        # Take either the middle or a corner piece, which makes it impossible to win (I think)
        for space in c_m:
            if space in possible_nums:
                possible_nums.remove(space)
                board.spaces[space] = AI_XO
                return possible_nums

    return AI_turn_easy(board, possible_nums, AI_XO)
