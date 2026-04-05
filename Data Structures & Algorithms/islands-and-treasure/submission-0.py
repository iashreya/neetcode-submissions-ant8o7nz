from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        # Multi-Source BFS; All 0 become our source
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while(queue):
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if ((0 <= nr < rows) and
                    (0 <= nc < cols) and
                    (grid[nr][nc] == 2147483647)):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        