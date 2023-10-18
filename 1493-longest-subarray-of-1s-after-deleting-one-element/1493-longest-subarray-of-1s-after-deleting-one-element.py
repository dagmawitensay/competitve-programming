class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counts = {'1': 0, '0': 0}
        longest = 0
        start = 0
        
        for end in range(len(nums)):
            counts[str(nums[end])] += 1
            while ((end - start + 1) - counts['1']) > 1 and start < end:
                counts[str(nums[start])] -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
        
        return longest - 1