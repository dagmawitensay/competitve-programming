class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}
        
        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        repeat = math.ceil(len(nums) / 2)
        
        for k, v in store.items():
            if v >= repeat:
                return k
        