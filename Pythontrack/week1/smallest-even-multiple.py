class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        
        org = n
        while True:
            n += org
            if n % 2 == 0:
                return n