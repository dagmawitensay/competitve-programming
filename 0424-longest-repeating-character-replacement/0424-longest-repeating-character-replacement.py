class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freqs = {}
        res = float('-inf')
        
        for end in range(len(s)):
            freqs[s[end]] = freqs.get(s[end], 0) + 1
            
            while (end - start + 1) - max(freqs.values()) > k:
                freqs[s[start]] = freqs[s[start]] - 1
                start += 1
                
            res = max(res, end - start + 1)
        
        return res