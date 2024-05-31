# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixXor = []
        res = 0

        for num in nums:
            res ^= num
            prefixXor.append(res ^ (2 ** (maximumBit) - 1))
        
        return prefixXor[::-1]







