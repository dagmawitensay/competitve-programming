class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                first , second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif char == '*':
                first , second = stack.pop(), stack.pop()
                stack.append(second * first)
            elif char == '/':
                denom = stack.pop()
                num = stack.pop()
                stack.append(int(num / denom))
            else:
                stack.append(int(char))
            
        
        return stack[0]