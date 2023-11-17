class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        max_sum = 0
        
        while l < r:
            max_sum = max(max_sum, nums[l] + nums[r])
            l += 1
            r -= 1
        
        return max_sum