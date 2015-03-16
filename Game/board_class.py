class Board():
    """The board for playing tic-tac-toe"""

    def __init__(self):

        self.spaces = {"1":"1", "2":"2", "3":"3", "4": "4",
                    "5":"5", "6":"6", "7":"7", "8":"8",
                    "9":"9"}
    def print_board(self):
        """ Print's the board in the format

                   |      |
                   |      |
                   |      |
           ------------------------
                   |      |
                   |      |
                   |      |
           ------------------------
                   |      |
                   |      |
                   |      |

        """
        first_row = "   {0}   |   {1}   |   {2}   ".format(self.spaces["1"], self.spaces["2"], self.spaces["3"])
        second_row = "   {0}   |   {1}   |   {2}   ".format(self.spaces["4"], self.spaces["5"], self.spaces["6"])
        third_row = "   {0}   |   {1}   |   {2}   ".format(self.spaces["7"], self.spaces["8"], self.spaces["9"])
        above_under = "       |       |       "
        in_between_rows = "------------------------"
        print(above_under + "\n" + first_row + "\n" + above_under + "\n" + in_between_rows + "\n" + above_under + "\n" +
        second_row + "\n" + above_under + "\n" + in_between_rows + "\n" + above_under + "\n" + third_row + "\n" + above_under)
