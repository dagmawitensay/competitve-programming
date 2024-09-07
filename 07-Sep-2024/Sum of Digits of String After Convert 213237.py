# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        chars = {chr(val + 97): val + 1 for val in range(26)}
        num = 0

        for char in s:
            val = 10 ** len(str(chars[char]))
            num = num * val + chars[char]

        
        while num >= 10 and k > 0:
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            num = digit_sum
            k -= 1

        return num