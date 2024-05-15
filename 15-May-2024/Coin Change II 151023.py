# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(currAmount, index):
            if currAmount < 0 or index >= len(coins):
                return 0
            
            if currAmount == 0:
                return 1
            
            if (currAmount, index) not in memo:
                memo[(currAmount, index)] = dp(currAmount, index + 1) + dp(currAmount - coins[index], index)
            return memo[(currAmount, index)]            
        
        return dp(amount, 0)

