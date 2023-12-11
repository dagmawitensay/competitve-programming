from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = Counter(arr)
        n = len(arr)
        mod = arr[0]
        
        for k, v in counts.items():
            if v >= ceil(n / 4):
                mod = k
        
        return mod