class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        res = 0
        x = abs(x)

        while x > 0:
            digit = x % 10
            x //= 10
            res = res * 10 + digit
     
        if res > (2 ** 31) or res < (-2 ** 31):
            return 0
        elif is_negative:
            return -1 * res
        return res
