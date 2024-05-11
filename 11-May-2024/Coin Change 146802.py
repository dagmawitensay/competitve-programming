# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(currAmount, memo):
            if currAmount < 0:
                return -1
            
            if currAmount == 0:
                return 0
            
            if currAmount in memo:
                return memo[currAmount]
            
            optimal = float('inf')
            
            for coin in coins:
                res = dp(currAmount - coin, memo)
                if res >= 0 and res < optimal:
                    optimal = res + 1
            
            memo[currAmount] = optimal if optimal != float('inf') else -1

            return memo[currAmount]
        
        if amount == 0:
            return 0
        
        return dp(amount, {})

