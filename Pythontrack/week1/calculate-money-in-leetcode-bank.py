class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remains = n % 7
        total = 0

        total += (28 * weeks + 7 * weeks  * (weeks - 1) // 2)
        for i in range(1, remains + 1):
            total += weeks + i
        
        return total