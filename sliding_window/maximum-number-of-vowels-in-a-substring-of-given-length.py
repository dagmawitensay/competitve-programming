class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        start = 0
        longest = 0
        counts = 0

        for end in range(len(s)):
            if s[end] in vowels:
                counts += 1
            
            if (end - start + 1) == k:
                longest = max(longest, counts)
                if s[start] in vowels:
                    counts -= 1
                start += 1
        
        return longest