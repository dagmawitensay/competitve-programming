class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Using kaden's algorithm
        """
        
        local_max = 0
        global_max = float('-inf')

        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)
        
        return global_max