MATRIX_MOVES = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
BLANK_POSITION = -1


class MyPlayer:
    """Player plays where he can get the most"""

    def __init__(self, my_color, opponent_color):
        self.lowest_priority_position = []
        self.name = "sobotvo2"
        self.my_color = my_color
        self.opponent_color = opponent_color
        self.board_size_row = 0
        self.board_size_collumn = 0
        self.board = None
        self.all_possible_moves = []

    def move(self, board):
        self.board_size_row = len(board)
        self.board_size_collumn = len(board[0])
        self.findLowPrioPositions()
        self.board = board
        self.findAllCorrectMoves(board)
        self.all_possible_moves = sorted(self.all_possible_moves, key=lambda l: l[2], reverse=True)
        if (len(self.all_possible_moves) == 0):
            return None
        else:
            return self.all_possible_moves[0][0], self.all_possible_moves[0][1]
        # return self.decideBestMove()

    def findAllCorrectMoves(self, board):
        for row in range(0, self.board_size_row):
            for collumn in range(0, self.board_size_collumn):
                if board[row][collumn] == self.my_color:
                    self.checkForMoves(board, row, collumn)

    def checkForMoves(self, board, row, collumn):
        for i in MATRIX_MOVES:
            score = 0
            position_checked_row = row + i[0]
            position_checked_collumn = collumn + i[1]
            while 0 <= position_checked_row < self.board_size_row and 0 <= position_checked_collumn < self.board_size_collumn:
                if board[position_checked_row][position_checked_collumn] == self.opponent_color:
                    position_checked_row += i[0]
                    position_checked_collumn += i[1]
                    score += 1
                elif board[position_checked_row][position_checked_collumn] == self.my_color:
                    break
                elif board[position_checked_row][position_checked_collumn] == BLANK_POSITION and score > 0:
                    self.all_possible_moves.append([position_checked_row, position_checked_collumn, score])
                    break
                else:
                    break

    def findLowPrioPositions(self):
        self.lowest_priority_position.append((1, 0))
        self.lowest_priority_position.append((1, 1))
        self.lowest_priority_position.append((0, 1))
        self.lowest_priority_position.append((0, self.board_size_collumn - 2))
        self.lowest_priority_position.append((1, self.board_size_collumn - 2))
        self.lowest_priority_position.append((1, self.board_size_collumn - 1))
        self.lowest_priority_position.append((self.board_size_row - 2, 0))
        self.lowest_priority_position.append((self.board_size_row - 2, 1))
        self.lowest_priority_position.append((self.board_size_row - 1, 1))
        self.lowest_priority_position.append((self.board_size_row - 2, self.board_size_collumn - 1))
        self.lowest_priority_position.append((self.board_size_row - 2, self.board_size_collumn - 2))
        self.lowest_priority_position.append((self.board_size_row - 1, self.board_size_collumn - 2))

    def decideBestMove(self):
        self.all_possible_moves = sorted(self.all_possible_moves, key=lambda l: l[2], reverse=True)
        while (1):
            find_optional = True
            for i in self.lowest_priority_position:
                if (self.all_possible_moves[0][0], self.all_possible_moves[0][1]) == (i[0], i[1]):
                    self.all_possible_moves.append([self.all_possible_moves[0][0], self.all_possible_moves[0][1], 0])
                    self.all_possible_moves.pop(0)
                    find_optional = False
            if find_optional:
                break
        return self.all_possible_moves[0][0], self.all_possible_moves[0][1]
