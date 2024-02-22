class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds = n // 2
        evens = n // 2 + (n % 2)

        def power(val, x):
            if x == 0:
                return 1
            elif x % 2 == 0:
                return (power((val * val) % (10 ** 9 + 7), x // 2)) % (10 ** 9 + 7)
            else:
                return ((val % (10 ** 9 + 7)) * power((val * val) % (10 ** 9 + 7) , x // 2)) % (10 ** 9 + 7)
        
        return (power(5, evens) * power(4, odds)) % (10 ** 9 + 7)
