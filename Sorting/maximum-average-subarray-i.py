class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        max_average = float('-inf')
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            if (r - l + 1) == k:
                average = curr_sum / k
                max_average = max(max_average, average)
                curr_sum -= nums[l]
                l += 1
       
        return max_average
            
        
