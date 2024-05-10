# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        def dp(index, sum1, sum2, memo):
            if index >= len(nums):
                return sum1 == target
            
            if (index, sum1, sum2) not in memo:
                memo[(index, sum1, sum2)] = dp(index+ 1, sum1 + nums[index], sum2, memo) or dp(index + 1, sum1, sum2 + nums[index], memo)
            
            return memo[(index, sum1, sum2)]
        
        if sum(nums) % 2 == 1:
            return False

        return dp(0, 0, 0, {})
