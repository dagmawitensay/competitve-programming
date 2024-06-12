# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # self.count = 0

        # @cache
        # def dp(currSum):
        #     if currSum == 0:
        #         return 1
            
        #     if currSum < 0:
        #         return 0 
        
        #     total = 0
        #     for num in nums:
        #         total += dp(currSum - num)
            
        #     return total
        
        # return dp(target)

        # bottom up

        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]