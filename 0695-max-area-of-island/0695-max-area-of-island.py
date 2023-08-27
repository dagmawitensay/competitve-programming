class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_area = 0
        count = 0
        def dfs(i, j):
            nonlocal count
            if grid[i][j]  == 1:
                count += 1
    
                grid[i][j] = 2
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for x, y in directions:
                    up, down = i + x, y + j

                    if up in range(n) and down in range(m) and grid[up][down] == 1:
                        dfs(up, down)
            else:
                return
        
        if not grid:
            return
        
        for i in range(n):
            for j in range(m):
                dfs(i, j)
                max_area = max(max_area, count)
                count = 0
        
        
        return max_area