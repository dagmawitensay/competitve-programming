class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remains = n % 7
        total = 0

        for i in range(1, weeks + 1):
            total += ((2 * i + 6) * 7) // 2
        
        total += ((2 * (weeks + 1) + remains - 1) * remains) // 2
        
        return total