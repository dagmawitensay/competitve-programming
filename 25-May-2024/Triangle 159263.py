# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(row, index):
            if row >= len(triangle) or index >= len(triangle[row]):
                return 0
            
            return min(triangle[row][index] + dp(row + 1, index), triangle[row][index] + dp(row + 1, index + 1))
        
        return dp(0, 0)