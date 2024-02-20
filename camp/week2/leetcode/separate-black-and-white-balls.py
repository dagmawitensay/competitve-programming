class Solution:
    def minimumSteps(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        zeros = 0
        count = 0
        r = len(s) - 1

        while r >= 0:
            if s[r] == '0':
                zeros += 1
            elif s[r] == '1':
                count += zeros
        
            r -= 1
        
        return count