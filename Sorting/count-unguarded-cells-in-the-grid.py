class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        grid = [[0] * n for i in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for row, col in guards:
            grid[row][col] = 'G'
        
        for row, col in walls:
            grid[row][col] = 'W'

        
        for row, col in guards:
            for x, y in directions:
                a, b = x, y
                # print(row + x, col + y)
                while isValid(row + x, col + y) and (grid[row + x][col + y] == 0 or grid[row + x][col + y] == 'V'):
                    grid[row + x][col + y] = 'V'
                    x += a
                    y += b
        
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    count += 1

        return count