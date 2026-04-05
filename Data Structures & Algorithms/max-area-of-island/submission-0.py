class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def dfs(r, c):
            if ((r < 0 or r >= rows) or
                (c < 0 or c >= cols) or
                (grid[r][c] == 0)):
                return 0

            grid[r][c] = 0
            left = dfs(r-1, c)
            right = dfs(r+1, c)
            up = dfs(r, c-1)
            down = dfs(r, c+1)
            return 1 + left + right + up + down

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area