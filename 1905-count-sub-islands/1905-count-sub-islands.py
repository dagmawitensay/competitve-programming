class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid2), len(grid2[0])
        count = 0
        
        def dfs(i, j):
            grid2[i][j] = 2
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for x, y in directions:
                up, down = x + i, y + j
                if up in range(n) and down in range(m) and grid2[up][down] == 1 and grid1[up][down] == 1:
                    dfs(up, down)
            
        
        if not grid2:
            return
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    dfs(i, j)
                    count += 1
    
        
        return count