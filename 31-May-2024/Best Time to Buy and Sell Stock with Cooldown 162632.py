# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        @cache
        def dp(i, j):
            if i >= len(prices):
                return 0
            
            if j == 0:
                return max(dp(i + 1, 0),  -prices[i] + dp(i + 1, 1))
            if j == 1:
                return max(dp(i + 1, 1), prices[i] + dp(i + 2, 0))
        
        
        return dp(0, 0)