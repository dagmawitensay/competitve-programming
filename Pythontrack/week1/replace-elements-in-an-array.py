class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexes = {}

        for i, v in enumerate(nums):
            indexes[v] = i

        for first, second in operations:
            nums[indexes[first]] = second
            indexes[second] = indexes[first]
            indexes.pop(first)

        return nums