class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(mid):
            curr = 0
            days = 1

            for weight in weights:
                if curr + weight > mid:
                    days += 1
                    curr = weight
                else:
                    curr += weight
            
            return days
        
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid) <= days:
                high = mid
            else:
                low = mid + 1
        
        return low