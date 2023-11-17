class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        if len(str(num)) < k:
            return 0
        
        s = str(num)
        start = 0
        count = 0
        for end in range(k - 1, len(s)):
            curr_str = s[start: end + 1]
            if int(curr_str) != 0 and num % int(curr_str) == 0:
                count += 1
            start += 1
        
        return count