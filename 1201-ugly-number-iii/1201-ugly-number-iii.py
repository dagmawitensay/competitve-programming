class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def enough(num):
            count = num//a + num//b + num//c - num//ab - num//bc - num//ac + num//abc
            return count >= n
        
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ac = math.lcm(a, c)
        abc = math.lcm(a, b, c)

        low = 1
        high = a * b * c

        while low < high:
            mid = low + (high - low) // 2
            if enough(mid):
                high = mid
            else:
                low = mid + 1
        
        return low