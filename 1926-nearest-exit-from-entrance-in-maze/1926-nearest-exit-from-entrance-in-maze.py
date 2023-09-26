from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(*entrance, 0)])
        n, m = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] == '+' 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def isBoundary(i, j):
            return (i == 0 or i == n - 1 or j == 0 or j == m - 1)
        
        while queue:
            x, y, c = queue.popleft()
            if (x == 0 or x == n-1 or y == 0 or y == m-1) and [x, y] != entrance:
                return c
            for dr, dc in directions:
                up, down = x + dr, y + dc
                if 0 <= up < n and 0 <= down < m and maze[up][down] == '.':
                    maze[up][down] = '+'
                    queue.append((up, down, c + 1))
        return -1