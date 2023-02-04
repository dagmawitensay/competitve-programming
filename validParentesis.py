class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        if len(s) < 2:
            return False
        for i in s:
            if i in "({[":
                self.stack.append(i)
            else:
                if self.stack == []:
                    return False
                top = self.stack[-1]
                if( (i == ')' and top == '(') or (i == '}' and top == '{') or (i == ']' and top == '[')):
                    self.stack.pop()
                else:
                    return False
        if self.stack == []:
            return True
        return False
    