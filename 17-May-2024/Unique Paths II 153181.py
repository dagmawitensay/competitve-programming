# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = 1

        def path(row, col):
            if 0 <= row < m and 0 <= col < n:
                return dp[row][col]
            
            return 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += path(i + 1, j) + path(i, j + 1)
        
        return dp[0][0]

