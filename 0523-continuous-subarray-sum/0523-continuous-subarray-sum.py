class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        store = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if k != 0:
                prefix %= k
            
            if prefix in store:
                if i - store[prefix] > 1:
                    return True
            
            else:
                store[prefix] = i
        
        return False