# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        min_avg = float('inf')
        min_index = 0

        for i in range(len(nums)):
            before = prefix[i] // (i + 1)
            if i != len(nums) - 1:
                after = (prefix[-1] - prefix[i]) // (len(nums) - i - 1)
            else:
                after = 0
            diff = abs(before - after)
            if diff < min_avg:
                min_avg = diff
                min_index = i
        
        return min_index