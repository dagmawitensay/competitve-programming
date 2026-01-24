class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            parts = 1
            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > threshold:
                    parts += 1
                    curr_sum = num
                    if parts > k:
                        return False
            
            if parts != k:
                return False
            
            return True
        
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

    
