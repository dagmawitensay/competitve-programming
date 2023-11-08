class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = (num, i)
    
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = nums[l][0] + nums[r][0]
            if curr_sum == target:
                return [nums[l][1], nums[r][1]]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
            