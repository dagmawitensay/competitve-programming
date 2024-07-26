# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_store = {}
        p_store = {}

        for i in range(len(s)):
            if s[i] in s_store and s_store[s[i]] != t[i]:
                return False
            
            if t[i] in p_store and p_store[t[i]] != s[i]:
                return False
            
            s_store[s[i]] = t[i]
            p_store[t[i]] = s[i]
            
        
        return True
