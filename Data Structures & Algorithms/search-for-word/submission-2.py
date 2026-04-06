class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i, seen):
            if ((r < 0 or r >= rows) or 
                (c < 0 or c >= cols) or
                (seen[r][c] == 1)):
                return False
                
            if board[r][c] != word[i]:
                return False

            if (i == len(word)-1 and board[r][c] == word[i]):
                return True

            directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
            seen[r][c] = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i+1, seen):
                    return True

            seen[r][c] = 0
            return False

        queue = []
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, [[0]*cols for _ in range(rows)]):
                        return True

        return False

        