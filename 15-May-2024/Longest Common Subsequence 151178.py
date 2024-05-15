# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(index1, index2):
            if index1 >= len(text1):
                return 0
            
            if index2 >= len(text2):
                return 0
            
            if (index1, index2) not in memo:
                res = 0
                if text1[index1] == text2[index2]:
                    res = 1 + dp(index1+ 1, index2 + 1)
                else:
                    res = max(dp(index1, index2 + 1), dp(index1 + 1, index2))
                
                memo[(index1, index2)] = res
            
            return memo[(index1, index2)]
            
        
        return dp(0, 0)