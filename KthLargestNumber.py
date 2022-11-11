class Solution:
    def kthLargestNumber(self,nums, k):
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        return nums[len(nums)-k]

