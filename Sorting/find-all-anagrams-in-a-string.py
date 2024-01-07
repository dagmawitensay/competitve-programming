from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = Counter(p)
        left = 0
        ans = []
        k = len(p)
        curr_count = Counter()

        for right in range(len(s)):
            curr_count[s[right]] = curr_count.get(s[right], 0) + 1
            if (right - left + 1) == k:
                if counts == curr_count:
                    ans.append(left)
                curr_count[s[left]] -= 1
                if not curr_count[s[left]]:
                    del curr_count[s[left]]
                
                left += 1
            
        return ans
                