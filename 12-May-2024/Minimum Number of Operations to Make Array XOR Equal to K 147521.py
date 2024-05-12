# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0

        for num in nums:
            res ^=  num
        
        count = 0
        maxVal = max(res, k)
        i = 0

        for i in range(32):
            count += 1 if ((res & 1 << i) ^ (k & 1 <<i)) else 0
        
        return count