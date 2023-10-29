class Solution:
    def decodeString(self, s: str) -> str:
        current_num = 0
        current_str = ""
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                current_num = current_num * 10 + int(s[i])
            elif s[i] == '[':
                stack.append(current_num)
                stack.append(current_str)
                current_num = 0
                current_str = ""
            elif s[i] == ']':
                prev_str = stack.pop()
                num = stack.pop()
                current_str = prev_str + num * current_str
            else:
                current_str += s[i]
        
        return current_str