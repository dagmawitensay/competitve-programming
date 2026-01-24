class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        def feasible(days):
            bouquets = 0 
            i = 0 

            while i < n:
                j = i
                while j < n and j < (i + k) and bloomDay[j] <= days:
                    j += 1
                
                if j == (i + k):
                    bouquets += 1
                    i = j
                else:
                    i += 1

                if bouquets == m:
                    return True
            
            return False
        
        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2
            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans