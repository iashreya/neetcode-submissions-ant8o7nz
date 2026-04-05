from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while(queue):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if ((0 <= nr < rows) and
                    (0 <= nc < cols) and
                    (grid[nr][nc] == 1)):
                    grid[nr][nc] = 1 + grid[r][c]
                    queue.append((nr,nc))

        timer = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                timer = max(timer, grid[r][c])

        return timer-2 if timer >= 2 else timer