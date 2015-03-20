import random

def AI_turn_easy(board, possible_nums, AI_XO):

    # generates a random, available space on the board and makes it an 'O'
    randChoice = random.choice(possible_nums)
    possible_nums.remove(randChoice)
    board.spaces[randChoice] = AI_XO

    return possible_nums

def avoid_losing_and_win_if_possible(board, possible_nums, AI_XO, p1_XO):

    # All of the possible winning configurations
    possible_configs = [["1", "2", "3"],
                        ["1", "4", "7"],
                        ["1", "5", "9"],
                        ["2", "5", "8"],
                        ["3", "6", "9"],
                        ["3", "5", "7"],
                        ["4", "5", "6"],
                        ["7", "8", "9"]]

    # Check each configuration; if there is two of the three spaces equal each other, put an 'O' in the other space
    for config in possible_configs:
        if board.spaces[config[0]] == AI_XO and board.spaces[config[0]] == board.spaces[config[1]]:
            if board.spaces[config[2]] in possible_nums:
                possible_nums.remove(board.spaces[config[2]])
                board.spaces[config[2]] = AI_XO
                return possible_nums
        elif board.spaces[config[0]] == AI_XO and board.spaces[config[0]] == board.spaces[config[2]]:
            if board.spaces[config[1]] in possible_nums:
                possible_nums.remove(board.spaces[config[1]])
                board.spaces[config[1]] = AI_XO
                return possible_nums
        elif board.spaces[config[1]] == AI_XO and board.spaces[config[1]] == board.spaces[config[2]]:
            if board.spaces[config[0]] in possible_nums:
                possible_nums.remove(board.spaces[config[0]])
                board.spaces[config[0]] = AI_XO
                return possible_nums
        elif board.spaces[config[0]] == p1_XO and board.spaces[config[0]] == board.spaces[config[1]]:
            if board.spaces[config[2]] in possible_nums:
                possible_nums.remove(board.spaces[config[2]])
                board.spaces[config[2]] = AI_XO
                return possible_nums
        elif board.spaces[config[0]] == p1_XO and board.spaces[config[0]] == board.spaces[config[2]]:
            if board.spaces[config[1]] in possible_nums:
                possible_nums.remove(board.spaces[config[1]])
                board.spaces[config[1]] = AI_XO
                return possible_nums
        elif board.spaces[config[1]] == p1_XO and board.spaces[config[1]] == board.spaces[config[2]]:
            if board.spaces[config[0]] in possible_nums:
                possible_nums.remove(board.spaces[config[0]])
                board.spaces[config[0]] = AI_XO
                return possible_nums
        else:
            pass
    return None

def AI_turn_hard(board, possible_nums, AI_XO, p1_XO):

    move = avoid_losing_and_win_if_possible(board, possible_nums, AI_XO, p1_XO)

    if move != None:
        return move
    else:
        return AI_turn_easy(board, possible_nums, AI_XO)


def AI_turn_impossible(board, possible_nums, AI_XO, p1_XO):

    move = avoid_losing_and_win_if_possible(board, possible_nums, AI_XO, p1_XO)

    if move != None:
        return move
    else:
        if '5' in possible_nums:
            possible_nums.remove('5')
            board.spaces['5'] = AI_XO
            return possible_nums
        else:
            side_spaces = ['8', '4', '2', '6']
            if board.spaces['1'] == p1_XO:
                if board.spaces['9'] == p1_XO:
                    random.shuffle(side_spaces)
                    for space in side_spaces:
                        if space in possible_nums:
                            possible_nums.remove(space)
                            board.spaces[space] = AI_XO
                            return possible_nums

            elif board.spaces['7'] == p1_XO:
                if board.spaces['3'] == p1_XO:
                    random.shuffle(side_spaces)
                    for space in side_spaces:
                        if space in possible_nums:
                            possible_nums.remove(space)
                            board.spaces[space] = AI_XO
                            return possible_nums

            else:
                corner_spaces = ['1', '7', '3', '9']
                random.shuffle(corner_spaces)
                for space in corner_spaces:
                    if space in possible_nums:
                        possible_nums.remove(space)
                        board.spaces[space] = AI_XO
                        return possible_nums

    if possible_nums != []:
        return AI_turn_easy(board, possible_nums, AI_XO)
