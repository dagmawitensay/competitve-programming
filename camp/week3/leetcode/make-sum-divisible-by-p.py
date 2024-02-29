class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_index = {0: -1}
        prefix = 0
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        if total < p:
            return -1
        
        min_length = len(nums)

        for i, num in enumerate(nums):
            prefix =  (prefix + num) % p
            val = (prefix - target + p) % p
            if val in sum_index:
                min_length = min(min_length, i - sum_index[val])
            sum_index[prefix] = i
    
        return min_length if min_length != len(nums) else -1