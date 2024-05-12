# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def dfs(row, col, count):
            count += grid[row][col]

            grid[row][col] = 0

            for x, y in directions:
                rowChange, colChange = x + row, y + col

                if isValid(rowChange, colChange) and grid[rowChange][colChange] != 0:
                    count = dfs(rowChange, colChange, count)
            
            return count
        

        maxFish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = dfs(i, j, 0)
                    maxFish = max(maxFish, res)
        
        return maxFish
