class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces_set = set(spaces)
        ans = ""

        for i in range(len(s)):
            if i in spaces_set:
                ans += " "
            
            ans += s[i]

        return ans