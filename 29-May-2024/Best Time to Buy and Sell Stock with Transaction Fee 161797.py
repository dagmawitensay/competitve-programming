# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @cache
        def dp(i, j):
            if i >= len(prices):
                return 0
            
            if j == 0:
                return max(dp(i + 1, 0), prices[i] + dp(i + 1, 1) - fee)
            
            if j == 1:
                return max(dp(i + 1, 1), -prices[i] + dp(i + 1, 0))
        
    
        return min(dp(0, 0), dp(0, 1))