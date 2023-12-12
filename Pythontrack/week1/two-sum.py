class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i, num in enumerate(nums):
            if target - num in num_indices:
                return [i, num_indices[target - num]]
            
            num_indices[num] = i
        