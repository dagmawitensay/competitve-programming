class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window_product = 1
        ans, start = 0, 0
        count = 0
        
        for end in range(len(nums)):
            window_product *= nums[end]
            while window_product >= k and start <= end:
                window_product /= nums[start]
                start += 1
            
            count += end - start + 1
        
        return count