class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        

        seen = set(s)
        for i, char in enumerate(s):
            if char.swapcase() not in seen:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i + 1:])
                
                return max(s1, s2, key=len)

        return s