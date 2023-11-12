class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        count = 0
        start = 0
        
        for end in range(2, len(s)):
            if len(set(s[start: end + 1])) == len(s[start: end + 1]):
                count += 1
            start += 1
            
        return count