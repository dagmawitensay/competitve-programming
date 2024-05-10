# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < cheap:
                cheap = prices[i]
            else:
                profit = max(profit, prices[i] - cheap)
        
        return profit