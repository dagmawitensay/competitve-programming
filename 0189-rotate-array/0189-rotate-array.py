class Solution:
     def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) < 2 ):
            return
        k = k % len(nums)
        temp = [None] * k
        temp += nums
        beg = 0
        end = len(temp) - k
        while beg < k:
            temp[beg], temp[end] = temp[end], temp[beg]
            beg += 1
            end +=1
        for i in range(len(nums)):
            nums[i] = temp[i]
