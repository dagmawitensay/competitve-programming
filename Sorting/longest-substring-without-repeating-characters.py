class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = {}
        start = 0
        longest = 0

        for end in range(len(s)):
            while start < len(s) and  s[end] in uniques:
                uniques[s[start]] -= 1
                if uniques[s[start]] == 0:
                    del uniques[s[start]]
                
                start += 1
            
            if s[end] not in uniques:
                uniques[s[end]] = 0
            
            uniques[s[end]] += 1
            longest = max(longest, end - start + 1)
        
        return longest

            