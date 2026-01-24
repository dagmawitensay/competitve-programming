class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2

        while left < right:
            mid = left + (right - left) // 2
            val = mid ** 2
            if val == x:
                return mid
            elif val < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left if left ** 2 <= x else left - 1