class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(capacity):
            days_needed = 1
            curr_load = 0
            for weight in weights:
                curr_load += weight
                if curr_load > capacity:
                    days_needed += 1
                    curr_load = weight
            
            return days_needed <= days
        
        l,r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if isPossible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
