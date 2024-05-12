# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # carry = False
        # n = max(a, b)
        # count = n.bit_length()
        
        # res = 0
        # for i in range(count):
        #     bit1, bit2 = a & 1, b & 1

        #     if bit1 == 0 and bit2 == 0:
        #         if carry:
        #             res |= 1 << i
        #             carry = False
        #         else:
        #             res &= ~(1 << i)
        #     elif bit1 ^ bit2:
        #         if carry:
        #             res &= ~(1 << i)
        #         else:
        #             res |= 1 << i
        #     else:
        #         if carry:
        #             res |= 1 << i
        #         else:
        #             res &= ~(1 << i)
        #             carry = True
        
        #     a >>= 1
        #     b >>= 1
        
        # if carry:
        #     res |= 1 << (count)
        
        # return res 

        # Not my code
        carry = 0
        mask = 0xfffff

        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return a & mask if b > mask else a

        