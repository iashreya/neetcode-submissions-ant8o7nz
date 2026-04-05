class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # check rows
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False
            seen = set()

        # check cols
        for col in range(9):
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False
            seen = set()

        # check boxes
        for col_off in range(0,9,3):
            for row_off in range(0,9,3):
                for row in range(3):
                    for col in range(3):
                        if board[row+row_off][col+col_off] != ".":
                            num = board[row + row_off][col + col_off]
                            if num not in seen:
                                seen.add(num)
                            else:
                                return False
                seen = set()
        
        return True

        
