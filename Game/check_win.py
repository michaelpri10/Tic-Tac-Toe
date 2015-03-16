def check_win(board, n):

    # All possible winning configurations
    possible_configs = [["1", "2", "3"],
                        ["1", "4", '7'],
                        ["1", "5", "9"],
                        ["2", "5", "8"],
                        ["3", "6", "9"],
                        ["3", "5", "7"],
                        ["4", "5", "6"],
                        ["7", "8", "9"]]

    for config in possible_configs:
        if board.spaces[config[0]] == board.spaces[config[1]] and board.spaces[config[0]] == board.spaces[config[2]]:
            return board.spaces[config[0]]
    if n == 9:
        return "draw"
    return None
