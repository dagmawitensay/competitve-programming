class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        res, cur_sum = 0, 0
        for n in nums:
            cur_sum += n
            if cur_sum - k in prefix_sums:
                res += prefix_sums[cur_sum - k]
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        return res
        