from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        if row == 0:
            return -1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            minutes_passed += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    up, down = r + dr, c + dc
                    if (up < 0 or down < 0 or up == row or down == col or grid[up][down] != 1):
                        continue
                    fresh -= 1
                    grid[up][down] = 2
                    queue.append((up, down))
        
        return minutes_passed if fresh == 0 else -1