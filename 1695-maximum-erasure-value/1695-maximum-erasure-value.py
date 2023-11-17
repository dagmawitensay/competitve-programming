class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counts = set()
        curr_sum = 0
        max_score = 0
        start = 0
        
        for end in range(len(nums)):
            while nums[end] in counts:
                counts.remove(nums[start])
                curr_sum -= nums[start]
                start += 1
            
            counts.add(nums[end])
            curr_sum += nums[end]
            max_score = max(max_score, curr_sum)
        
        return max_score
            
            
        