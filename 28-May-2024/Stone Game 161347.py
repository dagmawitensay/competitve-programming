# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(left, right):
            if left > right: 
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]

            if (right - left - len(piles)) % 2:
                memo[(left, right)] = max(piles[left] + dp(left + 1, right), piles[right] + dp(left,right - 1))
            else:
                memo[(left, right)] = min(-piles[left] + dp(left + 1, right), -piles[right] + dp(left, right - 1))
            return memo[(left, right)]

        return dp(0, len(piles) - 1) > 0