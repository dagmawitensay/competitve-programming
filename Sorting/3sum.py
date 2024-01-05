class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

    
        n = len(nums)
        nums.sort()
        ans = []
        visited = set()
        
        for i in range(n - 1):
            l, r = i + 1, n - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target and (nums[i], nums[l], nums[r]) not in visited:
                    visited.add((nums[i], nums[l], nums[r]))
                    ans.append((nums[i], nums[l], nums[r]))
                
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            
        return ans
                    
                    
            