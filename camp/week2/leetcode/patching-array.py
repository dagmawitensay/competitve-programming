class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        maxRange = 0
        index = 0

        while maxRange < n:
            if index < len(nums) and nums[index] <= maxRange + 1:
                maxRange += nums[index]
                index += 1
            else:
                maxRange += (maxRange + 1)
                count += 1
            
        return count