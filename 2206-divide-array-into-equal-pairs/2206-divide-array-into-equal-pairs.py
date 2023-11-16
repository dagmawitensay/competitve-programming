from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for k, v in counts.items():
            if v % 2 != 0:
                return False
        
        return True