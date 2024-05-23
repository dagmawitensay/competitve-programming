# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        index = {}
        dp = [0] * len(arr)
        maxLen = 0

        for i in range(len(arr)):
            prevVal = arr[i] - difference
            if prevVal in index:
                dp[i] = dp[index[prevVal]] + 1
            else:
                dp[i] = 1
            
            index[arr[i]] = i

            maxLen = max(maxLen, dp[i])
        
        return maxLen