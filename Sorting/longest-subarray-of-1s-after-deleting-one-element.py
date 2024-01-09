class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        left = 0
        k = 1

        for right in range(len(nums)):
            if not nums[right]:
                k -= 1
            
            while k < 0:
                if not nums[left]:
                    k += 1
                
                left += 1
            
            longest = max(longest, right - left)
        
        return longest