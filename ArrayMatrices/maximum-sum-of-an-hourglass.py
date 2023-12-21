class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        glass_neigbors = [(-1, -1), (1, 1), (-1, 0), (1, 0), (1, -1), (-1, 1)]
        max_sum = float('-inf')

        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
        
        for i in range(m):
            for j in range(n):
                vals = []
                for x, y in glass_neigbors:
                    if not isValid(i + x, j + y):
                        break
                    else:
                        vals.append(grid[i + x][y + j])
                
                if len(vals) == 6:
                    max_sum = max(sum(vals) + grid[i][j], max_sum)
        
        return max_sum
                
