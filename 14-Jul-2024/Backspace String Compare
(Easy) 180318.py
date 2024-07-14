# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for i in s:
            if stack and i == '#':
                stack.pop()
            elif i != '#':
                stack.append(i)
        
        for j in t:
            if stack2 and  j == '#':
                stack2.pop()
            elif j != '#':
                stack2.append(j)
        print(stack, stack2)
        return stack == stack2