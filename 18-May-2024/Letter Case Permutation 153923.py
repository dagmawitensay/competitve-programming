# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        visited = set()
        def backtrack(index, current):
            if len(current) == len(s):
                ans.add("".join(current))
            
            if index >= len(s):
                return
            
            for i in range(index, len(s)):
                current.append(s[index])
                backtrack(i + 1, current)
                current.pop()
                current.append(s[index].swapcase())
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return ans