class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if count == 1:
                    return False
                
                count += 1

                if (i - 2) >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        
        return True