class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                target_sum = nums[i] + nums[l] + nums[r]
                if abs(target - target_sum) < diff:
                    diff = abs(target - target_sum)
                    closest = target_sum
                elif target_sum < target:
                    l += 1
                elif target_sum > target:
                    r -= 1
                else:
                    return target_sum
            
        return closest