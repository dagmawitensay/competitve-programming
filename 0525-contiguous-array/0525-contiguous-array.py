class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0: -1}
        count = 0
        longest = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in counts:
                longest = max(longest, i - counts[count])
            else:
                counts[count] = i
        
        return longest