class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        if num < 3:
            return []
        
        l, r = 0, num
        mid = 16
        while l < r:
            mid = (l + r) // 2
            a, b, c = mid - 1, mid, mid + 1
            if a + b + c == num:
                return [a, b, c]
            elif a + b + c < num:
                l = mid + 1
            else:
                r = mid
        
        return []