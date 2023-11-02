class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        ans = []
        
        for i in range(len(nums)):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]
            left_count = i
            right_count = len(nums) - i - 1
            
            left_val = left_count * nums[i] - left_sum
            right_val = right_sum - right_count * nums[i]
                
            ans.append(left_val + right_val)
        
        return ans