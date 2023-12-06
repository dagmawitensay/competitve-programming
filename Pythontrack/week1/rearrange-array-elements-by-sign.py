class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_index = 0
        neg_index = 1
        ans = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                ans[neg_index] = nums[i]
                neg_index += 2
        
        return ans
