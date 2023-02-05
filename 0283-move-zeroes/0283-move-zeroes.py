class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        for val in range(len(nums)):
            if nums[val] != 0:
                nums[first] , nums[val] = nums[val], nums[first]
                first += 1
        