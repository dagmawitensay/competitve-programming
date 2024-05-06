# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalXor = 0
        numXor = 0
        for i in range(len(nums)+ 1):
            totalXor ^= i
        
        for val in nums:
            numXor ^= val
        
        return totalXor ^ numXor
        
