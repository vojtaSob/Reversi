MATRIX_MOVES = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
BLANK_POSITION = -1
POSITION_RANKS_MID = [
    [10, -10, 2, 2, 2, 2, -10, 10],
    [-10, -10, -1, -1, -1, -1, -10, -10],
    [2, -1, 0, 0, 0, 0, -1, 5],
    [2, -1, 0, 0, 0, 0, -1, 5],
    [2, -1, 0, 0, 0, 0, -1, 5],
    [2, -1, 0, 0, 0, 0, -1, 5],
    [-10, -10, -1, -1, -1, -1, -10, -10],
    [10, -10, 2, 2, 2, 2, -10, 10],
]
POSITION_RANKS_EARLY = [
    [5, 0, 0, 0, 0, 0, 0, 5],
    [0, -5, 2, 2, 2, 2, -5, 0],
    [0, 2, 5, 3, 3, 5, 2, 0],
    [0, 2, 3, 0, 0, 3, 2, 0],
    [0, 2, 3, 0, 0, 3, 2, 0],
    [0, 2, 5, 3, 3, 5, 2, 0],
    [0, -5, 2, 2, 2, 2, -5, 0],
    [5, 0, 0, 0, 0, 0, 0, 5],
]
POSITION_RANKS_LATE = [
    [5, -4, 0, 0, 0, 0, -4, 5],
    [-4, -5, 0, 0, 0, 0, -4, -4],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-4, -4, 0, 0, 0, 0 - 4, -4],
    [5, -4, 0, 0, 0, 0, -4, 5],
]


class MyPlayer:
    """Player plays where he can get the most"""

    def __init__(self, my_color, opponent_color):
        self.name = "sobotvo2"
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board_size_row = 0
        self.board_size_column = 0
        self.board = None
        self.all_possible_moves = []

    def move(self, board):
        self.board_size_row = len(board)
        self.board_size_column = len(board[0])
        self.board = board
        self.findAllCorrectMoves(board)
        self.all_possible_moves = sorted(self.all_possible_moves, key=lambda l: l[2], reverse=True)
        if len(self.all_possible_moves) == 0:
            return None
        else:
            return self.decideBestMove()

    def findAllCorrectMoves(self, board):
        for row in range(0, self.board_size_row):
            for column in range(0, self.board_size_column):
                if board[row][column] == self.my_color:
                    self.checkForMoves(board, row, column)

    def checkForMoves(self, board, row, column):
        for i in MATRIX_MOVES:
            score = 0
            position_checked_row = row + i[0]
            position_checked_column = column + i[1]
            while 0 <= position_checked_row < self.board_size_row and 0 <= position_checked_column < self.board_size_column:
                if board[position_checked_row][position_checked_column] == self.opponent_color:
                    position_checked_row += i[0]
                    position_checked_column += i[1]
                    score += 1
                elif board[position_checked_row][position_checked_column] == self.my_color:
                    break
                elif board[position_checked_row][position_checked_column] == BLANK_POSITION and score > 0:
                    self.all_possible_moves.append([position_checked_row, position_checked_column,
                                                    score + POSITION_RANKS_EARLY[position_checked_row][
                                                        position_checked_column]])
                    break
                else:
                    break

    def decideBestMove(self):
        self.all_possible_moves = sorted(self.all_possible_moves, key=lambda l: l[2], reverse=True)
        print(self.all_possible_moves[0])
        return self.all_possible_moves[0][0], self.all_possible_moves[0][1]
