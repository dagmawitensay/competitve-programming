class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        j = 0
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                nums[j] = nums[i]
                j += 1
        
        return j
                