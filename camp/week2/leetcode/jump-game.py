class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        good = len(nums) - 1
        prev = len(nums) - 2

        while prev >= 0:
            if nums[prev] + prev >= good:
                good = prev
                prev -= 1
            else:
                prev -= 1
            
            if good == 0:
                return True
        
        return False
