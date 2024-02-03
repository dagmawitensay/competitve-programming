class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0 or nums is None:
            return nums

        solution = [1] * length
        for i in range(1, length):
            solution[i] = nums[i - 1] * solution[i - 1]

        right_product = 1
        for i in range(length - 1, -1, -1):
            solution[i] *= right_product
            right_product *= nums[i]

        return solution