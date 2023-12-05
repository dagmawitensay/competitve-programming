class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += n // 2
            if n % 2 == 0:
                n //= 2
            else:
                n //= 2
                n += 1
        
        return matches