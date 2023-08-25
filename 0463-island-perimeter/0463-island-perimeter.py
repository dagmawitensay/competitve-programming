class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
    
        def dfs(grid, row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 1
            
            if grid[row][col] == 2:
                return 0
            
            grid[row][col] = 2
            
            return dfs(grid, row + 1, col) + dfs(grid, row - 1, col)  + dfs(grid, row, col + 1) + dfs(grid, row, col - 1)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
        
        