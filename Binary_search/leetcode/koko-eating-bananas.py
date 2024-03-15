class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        def isPossible(bananas):
            hours = 0
            
            for pile in piles:
                hours += ceil(pile / bananas)

            return hours

        
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid) <= h:
                high = mid
            else:
                low = mid + 1
        
        return low