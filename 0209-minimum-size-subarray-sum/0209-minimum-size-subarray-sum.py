class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        window_sum = 0
        left = 0
        
        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        if ans == float('inf'):
            return 0
        
        return ans