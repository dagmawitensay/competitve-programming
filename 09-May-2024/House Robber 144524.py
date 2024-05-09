# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dp(index):
            if index >= len(nums):
                return 0
            
            if memo[index] == -1:
                memo[index] = max(dp(index + 1), dp(index + 2) + nums[index])
            
            return memo[index]
        
        return dp(0)