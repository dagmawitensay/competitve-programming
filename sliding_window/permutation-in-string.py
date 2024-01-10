from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p_count = Counter(s1)
        s_count = Counter()
        start, k = 0, len(s1)

        for end in range(len(s2)):
            s_count[s2[end]] += 1
            if (end - start + 1) == k:
                if s_count == p_count:
                    return True
                
                s_count[s2[start]] -= 1
                if s_count[s2[start]] == 0:
                    del s_count[s2[start]]
                start += 1
        
        return False