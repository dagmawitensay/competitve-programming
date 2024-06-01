# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, j, count):
            if i >= len(prices) or count > 1:
                return 0
            
            if j == 0:
                return max(dp(i + 1, 0, count), -prices[i] + dp(i + 1, 1, count))
            
            if j == 1:
                return max(dp(i + 1, 1, count), prices[i] + dp(i + 1, 0, count + 1))
            
    
        return dp(0, 0, 0)
