# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Top Down DP
        memo = {}
        def dp(index1, index2):
            if index1 >= len(s):
                return True
            if index2 >= len(t):
                return False
            
            if (index1, index2) not in memo:
                if s[index1] == t[index2]:
                    res = dp(index1 + 1, index2 + 1)
                else:
                    res = dp(index1, index2 + 1)
                
                memo[(index1, index2)] = res
            
            return memo[(index1, index2)]
        
        return dp(0, 0)