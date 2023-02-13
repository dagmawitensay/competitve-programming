class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0]
        privot_index = -1
        for i in range(len(nums)):
            pre_sum.append(pre_sum[i] + nums[i])
        pre_sum = pre_sum[1:]
        for i in range(len(pre_sum)):
            if i == 0:
                left_sum = 0
                right_sum = pre_sum[-1] - pre_sum[0]
            elif i == len(pre_sum) - 1:
                right_sum = 0
                left_sum = pre_sum[i - 1]
            else:
                left_sum = pre_sum[i - 1]
                right_sum = pre_sum[-1] - pre_sum[i]
            if left_sum == right_sum:
                privot_index = i
                return privot_index
        return privot_index
            
