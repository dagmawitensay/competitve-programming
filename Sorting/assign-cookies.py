class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        first, second = 0, 0

        while first < len(g) and second < len(s):
            if s[second] >= g[first]:
                first += 1
                second += 1
            else:
                second += 1
        
        return first