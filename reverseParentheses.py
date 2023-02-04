def  reverseParentheses(s):
    stack = []
    for i in s:
        if i != ')':
            stack.append(i)
        else:
            top  = stack[-1]
            temp = ''
            while top != '(':
                temp += stack.pop()
                top = stack[-1]
            stack.pop()
            for i in temp:
                stack.append(i)
    return ''.join(stack)
