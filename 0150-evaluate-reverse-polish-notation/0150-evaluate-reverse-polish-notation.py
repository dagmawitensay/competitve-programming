class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        if len(tokens) == 1:
            return int(tokens[-1])
        for token in tokens:
            if token not in "+-*/":
                self.stack.append(token)
            else:
                match token:
                    case '+':
                        second, first = int(self.stack.pop()), int(self.stack.pop())
                        self.stack.append(first + second)
                    case '-':
                        second, first = int(self.stack.pop()), int(self.stack.pop())
                        self.stack.append(first - second)
                    case '*':
                        second, first = int(self.stack.pop()), int(self.stack.pop())
                        self.stack.append(first * second)
                    case '/':
                        second, first = int(self.stack.pop()), int(self.stack.pop())
                        self.stack.append(int(first / second))
        return self.stack[-1]