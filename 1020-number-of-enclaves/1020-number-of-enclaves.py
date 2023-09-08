class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            if i not in range(n) or j not in range(m) or grid[i][j] == 0:
                return 
            
            grid[i][j] = 0
            for x, y in directions:
                up, down = x + i, y + j
                dfs(up, down)
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n -1 or j == 0 or j == m - 1:
                    if grid[i][j] == 1:
                        dfs(i, j)
        
        
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                    
        return count