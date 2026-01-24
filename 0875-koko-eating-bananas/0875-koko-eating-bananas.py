class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            hours = 0

            for pile in piles:
                if pile < k:
                    hours += 1
                else:
                    hours += pile // k
                    if pile % k != 0:
                        hours += 1
                
                if hours > h:
                    return False
            
            return True
  
        left = min(piles)
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left