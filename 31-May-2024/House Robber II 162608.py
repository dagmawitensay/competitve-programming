# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(index, flag = False):
            if index >= len(nums):
                return 0   

            if index == 0:
                right = dp(index + 2, True) + nums[index]
            elif index == len(nums) - 1 and flag:
                return 0
            else:
                right = dp(index + 2, flag) + nums[index]

            return max(dp(index + 1, flag), right)
        
        return dp(0)
