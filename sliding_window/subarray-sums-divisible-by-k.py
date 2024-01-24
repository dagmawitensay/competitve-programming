class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        res, cur_sum = 0, 0
        
        for n in nums:
            cur_sum = (cur_sum + n % k + k) % k
            if cur_sum  in prefix_sums:
                res += prefix_sums[cur_sum]
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
            
        return res