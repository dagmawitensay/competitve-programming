# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        def isdigit(val):
            try:
                n = int(val)
                return True
            except:
                return False

        for operation in operations:
            if isdigit(operation):
                stack.append(int(operation))
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(2 * stack[-1])
            else:
                stack.pop()
        
        return sum(stack)