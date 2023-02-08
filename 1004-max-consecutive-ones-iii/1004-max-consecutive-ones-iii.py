class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowstart = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            if (k < 0):
                if nums[windowstart] == 0:
                    k += 1
                windowstart += 1
        return i - windowstart + 1
        
            


