class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            grid[i][j] = '2'
            directions = [(0, 1), (0, - 1), (1, 0), (-1, 0)]
            
            for x, y in directions:
                up, down = x + i, y + j
                if up in range(n) and down in range(m) and grid[up][down] == '1':
                    dfs(up, down)
        
        
        if not grid:
            return
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        
        return count