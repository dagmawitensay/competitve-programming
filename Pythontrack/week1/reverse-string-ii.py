class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        indices = [i for i in range(0, len(s), 2 * k)]
        i, j = 0, 0
        ans = []

        while i < len(s):
            if j < len(indices):
                if i < indices[j]:
                    ans.append(s[i])
                    i += 1
                else:
                    ans.append(s[i:i+k][::-1])
                    i += k
                    j += 1
            else:
                break
        
        while i < len(s):
            ans.append(s[i])
            i += 1

        
        return "".join(ans)
        