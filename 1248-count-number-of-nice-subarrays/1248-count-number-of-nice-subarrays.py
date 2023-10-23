class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_sum = 0
        store = {}
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
            
        store[0] = 1
        for num in nums:
            odd_sum += num
            store[odd_sum] = store.get(odd_sum, 0) + 1
            
            if odd_sum - k in store:
                count += store[odd_sum - k]
        
        return count