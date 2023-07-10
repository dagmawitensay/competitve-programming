class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        curr_sum = 0
        max_average = float('-inf')
        
        while end < len(nums):
            if k != (end - start):
                curr_sum += nums[end]

            if k == (end - start + 1):
                max_average = max(max_average , curr_sum)
                curr_sum -= nums[start]
                start += 1
        
            end += 1
            
        return max_average / float(k)