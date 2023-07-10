class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_occurences = {s[i]: i for i in range(n)}
        size, end = 0, 0
        res = []
        
        for i in range(n):
            size += 1
            end = max(end, last_occurences[s[i]])
            
            if i == end:
                res.append(size)
                size = 0
        
        return res