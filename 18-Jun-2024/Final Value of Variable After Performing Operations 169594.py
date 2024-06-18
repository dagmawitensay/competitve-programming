# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0

        for operator in operations:
            if operator == '--X' or operator == 'X--':
                total -= 1
            elif operator == 'X++' or operator == '++X':
                total += 1
        
        return total
