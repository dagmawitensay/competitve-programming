class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sums = {0: 1}
        res, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            if curr_sum - goal in prefix_sums:
                res += prefix_sums[curr_sum - goal]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
        return res