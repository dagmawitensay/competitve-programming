class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        res = 0
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10
            res = res * 10 + digit
        
        return -1 * res if is_negative else res
