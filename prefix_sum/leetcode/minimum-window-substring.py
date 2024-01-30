class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = len(s)
        def isValid(dict1, dict2):
            for key, val in dict2.items():
                if val > dict1[key]:
                    return False
            return True

        t_count = Counter(t)
        s_count = Counter()
        start = 0
        ans = ""
        min_length = float('inf')

        for end in range(len(s)):
            if s[end] in t_count:
                s_count[s[end]] += 1
            
            while isValid(s_count, t_count):
                if (end - start + 1) < min_length:
                    min_length = end - start + 1
                    ans = s[start: end + 1]
                s_count[s[start]] -= 1
                start += 1
        
        return ans

        