from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        ans = []

        for val in arr2:
            ans.extend([val] * counts[val])
            del counts[val]
        
        remains = []
        for k, v in counts.items():
            remains.extend([k] * v)
            
        remains.sort()
        ans.extend(remains)
        
        return ans
        