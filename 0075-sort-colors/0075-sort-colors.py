class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store = [0] * 3
        
        for i in range(len(nums)):
            store[nums[i]] += 1
        
        j = 0
        
        for i in range(len(store)):
            while store[i] > 0:
                nums[j] = i
                j += 1
                store[i] -= 1
    
                
            
            
        
            