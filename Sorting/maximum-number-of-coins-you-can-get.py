class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        index = len(piles) // 3

        piles.sort()
        max_coins = 0
        for i in range(index, len(piles), 2):
            max_coins += piles[i]
        
        return max_coins