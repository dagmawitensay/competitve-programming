class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(piles, k, h):
            hours = [ceil(pile / k) for pile in piles]

            return sum(hours) <= h
    
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if isPossible(piles, mid, h):
                r = mid
            else:
                l = mid + 1
        
        return l