# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(i, sumVal):
            if sumVal == n:
                return 1
            
            if sumVal >= n or i >= n:
                return float('-inf')
            
            return max(i * dp(i, sumVal + i), dp(i + 1, sumVal))
        
        return dp(1, 0)