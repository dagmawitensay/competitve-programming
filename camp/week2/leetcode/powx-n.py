class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/ x, -n)
        if n == 0:
            return 1
        elif n % 2 == 0:
            squared = (x * x)
            return (self.myPow(squared, n // 2))
        else:
            squared = (x * x)
            return (x * self.myPow(squared, n // 2))