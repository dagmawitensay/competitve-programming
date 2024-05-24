# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        current = []
        def dp(index):
            if index >= len(s):
                ans.append(current.copy())
                return
            
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    current.append(s[index: i + 1])
                    dp(i + 1)
                    current.pop()
        
        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        dp(0)
        return ans
            
            
            
            
