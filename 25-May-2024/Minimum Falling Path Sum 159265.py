# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n

        @cache
        def dp(row, col):
            if not isValid(row, col):
                return 0 if row >= n else float('inf')
            
            return min(matrix[row][col] + dp(row + 1, col -1), matrix[row][col] + dp(row + 1, col), matrix[row][col] + dp(row + 1, col + 1))
        

        minPathSum = float('inf')
        for i in range(n):
            res = dp(0, i)
            minPathSum = min(minPathSum, dp(0, i))
        
        return minPathSum

