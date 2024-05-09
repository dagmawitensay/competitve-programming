# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        count = num.bit_length()
        num ^= (1 << count) - 1

        return num
