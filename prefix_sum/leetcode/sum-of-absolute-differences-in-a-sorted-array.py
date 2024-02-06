class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum = 0
        ans = []
        total = sum(nums)
        n = len(nums)

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            left_val = i * nums[i] - left_sum
            right_val = right_sum - (n - 1 - i) * nums[i]

            ans.append(right_val + left_val)
            left_sum += nums[i]
        
        return ans

