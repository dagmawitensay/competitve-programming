class Solution:
    def isValid(self, s: str) -> bool:
        opens = "({["
        stack = []

        for i in range(len(s)):
            if s[i] in opens:
                stack.append(s[i])
            else:
                if stack:
                    if stack[-1] == '{' and s[i] == '}':
                        stack.pop()
                    elif stack[-1] == '(' and s[i] == ')':
                        stack.pop()
                    elif stack[-1] == '[' and s[i] == ']':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        
        return True