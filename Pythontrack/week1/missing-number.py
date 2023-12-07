class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_val = len(nums)
        vals_set = set(nums)

        for i in range(max_val + 1):
            if i not in vals_set:
                return i