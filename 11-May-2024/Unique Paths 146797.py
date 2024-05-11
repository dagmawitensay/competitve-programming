# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def __init__(self):
        self.paths = 0
    def uniquePaths(self, m: int, n: int) -> int:
        def isValid(row, col):
            return row < m and col < n

        memo = {}
        def dp(row, col):
            if not isValid(row, col):
                return 0

            if (row, col) == (m - 1, n - 1):
                return 1
            
            if (row, col) not in memo:
                memo[(row, col)] = dp(row + 1, col) + dp(row, col + 1)
            
            return memo[(row, col)]
        
        return dp(0, 0)