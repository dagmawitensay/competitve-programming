class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        def backtrack(i, sub):
            if i >= len(nums):
                return
            
            sub.append(nums[i])
            if sub not in subsets:
                    subsets.append(sub[:])
            backtrack(i + 1, sub)
            sub.pop()
            backtrack(i + 1, sub)
        
        backtrack(0, [])
        
        return subsets