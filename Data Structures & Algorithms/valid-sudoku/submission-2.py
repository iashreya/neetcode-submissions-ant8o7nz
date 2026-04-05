class Solution:
    def __init__(self):
        self.digits = {i:0 for i in range(0, 10)}

    def checkColumns(self, board):
        for col in range(9):
            for row in range(9):
                # print(board[row][col], self.digits)
                self.digits[board[row][col]] += 1
            if not self.checkDigits():
                return False
            self.resetDigits()
        return True

    def checkRows(self, board):
        for row in range(9):
            for col in range(9):
                self.digits[board[row][col]] += 1
            if not self.checkDigits():
                return False
            self.resetDigits()
        return True

    def checkSquares(self, board):
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                for row in range(3):
                    for col in range(3):
                        self.digits[board[row + box_row][col + box_col]] += 1
                if not self.checkDigits():
                    return False
                self.resetDigits()
        return True

    def checkDigits(self):
        for digit, count in self.digits.items():
            if digit != 0 and count > 1:
                return False
        return True

    def resetDigits(self):
        self.digits = {i:0 for i in range(10)}

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    board[row][col] = 0
                else:
                    board[row][col] = int(board[row][col])

        col = self.checkColumns(board)
        row = self.checkRows(board)
        box = self.checkSquares(board)

        print(col, row, box)

        return col and row and box