# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        before = n
        n = self.divisorSum(n)
        while before != n:
            before = n
            n = self.divisorSum(n)
        
        return n

    def divisorSum(self, n):
        d = 2
        sum = 0
        while d * d <= n:
            while n % d == 0:
                sum += d
                n //= d
            
            d += 1
        
        if n > 1:
            sum += n
        
        return sum
