# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num
        
        setBit = (res & res - 1) ^ res

        ones = 0
        zeros = 0

        for num in nums:
            if num & setBit:
                ones ^= num
            else:
                zeros ^= num
        
        return [ones, zeros]