class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = 0
        max_val = nums[0]

        for i in range(len(nums)):
            prefix += nums[i]
            average = ceil(prefix / (i + 1))
            max_val = max(max_val, average)
        
        return max_val