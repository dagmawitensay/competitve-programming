class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[i] + nums[i])
        min_start = min(pre_sum)
        if (min_start) > 0:
            return min_start
        return abs(min_start) + 1
        
        
        