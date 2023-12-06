from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        repeat = len(nums) // 3
    
        for k, v in counts.items():
            if v > repeat:
                result.append(k)
        
        return result