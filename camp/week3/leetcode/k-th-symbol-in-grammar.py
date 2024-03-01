class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        if k % 2 == 1:
            val = self.kthGrammar(n - 1, (k + 1) // 2)
            return val
        elif k % 2 == 0:
            val = self.kthGrammar(n - 1, k // 2)
            return abs(val - 1)