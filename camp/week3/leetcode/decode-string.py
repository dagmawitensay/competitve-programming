class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            res = []
            k = 0

            while index < len(s):
                if s[index].isdigit():
                    k = k * 10 + int(s[index])
                elif s[index] == '[':
                    index, decoded = helper(index + 1)
                    res.append(k * decoded)
                    k = 0
                elif s[index] == ']':
                    return index, "".join(res)
                else:
                    res.append(s[index])
                index += 1
            
            return index, "".join(res)
        
        return helper(0)[1]