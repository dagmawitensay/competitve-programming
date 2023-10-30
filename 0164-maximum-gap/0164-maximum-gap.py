class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        nums.sort()
        max_diff = float('-inf')
        l, r = 0, 1
        
        while r < len(nums):
            max_diff = max(max_diff, nums[r] - nums[l])
            l += 1
            r += 1
        
        return max_diff