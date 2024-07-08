# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        store = {}
        result = []
        for i, word in enumerate(strs):
            anagram = tuple(sorted(word))
            if anagram in store:
                store[anagram].append(i)
            else:
                store[anagram] = [i]
        
        for k, v in store.items():
            curr = []
            for i in v:
                curr.append(strs[i])
            result.append(curr)
        
        return result