class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        longest = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if not strs[j].startswith(strs[0][:i + 1]):
                    break
            else:
                longest = strs[0][:i + 1]
        
        return longest
                    