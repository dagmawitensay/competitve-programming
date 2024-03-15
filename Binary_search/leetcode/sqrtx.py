class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x // 2

        while low <= high:
            mid = (low + high) // 2
            if (mid ** 2) > x:
                high = mid - 1
            elif (mid ** 2) < x:
                low = mid + 1
            else:
                return mid
        
        return low - 1 if (low != 0  and low != 1) else x

