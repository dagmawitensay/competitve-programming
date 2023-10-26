class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        store = {}
        ans = []
        start, end = 0, 9
        if len(s) < 10:
            return []
        
        while end < len(s):
            store[s[start: end + 1]] = store.get(s[start: end + 1], 0) + 1
            start += 1
            end += 1
        
        for k, v in store.items():
            if v > 1:
                ans.append(k)
        
        return ans