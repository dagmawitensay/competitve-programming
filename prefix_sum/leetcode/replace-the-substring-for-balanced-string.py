class Solution:
    def balancedString(self, s: str) -> int:
        counts = Counter(s)
        threshold = len(s) // 4
        extra = Counter()
        start = 0
        min_length = len(s)

        for key, val in counts.items():
            if val > threshold:
                extra[key] = val - threshold
            
        if extra == Counter():
            return 0
        
        curr_chars = Counter()
        
        for end in range(len(s)):
            curr_chars[s[end]] += 1
            while extra - curr_chars == Counter():
                min_length = min(min_length, end - start + 1)
                curr_chars[s[start]] -= 1
                start += 1
    
        return min_length