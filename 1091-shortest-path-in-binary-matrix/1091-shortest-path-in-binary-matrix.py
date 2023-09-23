from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        shortest_path = float('inf')
        row, col = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        if row == 1 and col == 1:
            return 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1),(1, -1), (1, 1)]
        
        while queue:
            for i in range(len(queue)):
                r, c, dist = queue.popleft()
                for dr, dc in directions:
                    up, down = r + dr, c + dc
                    if up < 0 or down < 0 or up == row or down == col or grid[up][down] == 1:
                        continue
                    elif up == row - 1 and down == col - 1:
                        shortest_path = min(shortest_path, dist + 1)

                    else:
                        grid[up][down] = 1
                        queue.append((up, down, dist + 1))

        return shortest_path if shortest_path != float('inf') else -1
            