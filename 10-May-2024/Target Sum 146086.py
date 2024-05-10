# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def __init__(self):
        self.count = 0
        self.memo = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(index, val):
            if index >= len(nums):
                if val == target:
                    return 1
                return 0
            
            if (index, val) not in self.memo:
                self.memo[(index, val)] = dp(index + 1, val + nums[index]) + dp(index + 1, val - nums[index])
            return self.memo[(index, val)]
        
        return dp(0, 0)

            
