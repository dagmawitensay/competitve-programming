class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tempstr = "".join([char for char in s if char.isalpha() or char.isdigit()])
        l, r = 0, len(tempstr) - 1
        
        while l < r:
            if tempstr[l] != tempstr[r]:
                return False
            l += 1
            r -= 1
        
        return True