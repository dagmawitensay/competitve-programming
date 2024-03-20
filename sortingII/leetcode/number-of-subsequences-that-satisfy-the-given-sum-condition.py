class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        MOD = 10 ** 9 + 7
        nums.sort()

        for i in range(len(nums)):
            val = target - nums[i]
            end = bisect_right(nums, val)  - 1
            res += (pow(2, end - i)) % MOD
        
        return int(res % MOD)


