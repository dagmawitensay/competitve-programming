class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        prefix = 0
        subarrays = 0

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in sum_count:
                subarrays += sum_count[prefix - k]
            
            sum_count[prefix] = sum_count.get(prefix, 0) + 1
        
        return subarrays