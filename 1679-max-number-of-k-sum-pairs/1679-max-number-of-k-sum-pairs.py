class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        ctr = 0
        nums.sort()
        
        while left < right and nums:
            if nums[left] + nums[right] == k:
                ctr += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        
        return ctr