class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        visited = set()
        def backtrack(index):
            if tuple(subset) not in visited:
                visited.add(tuple(subset))
                ans.append(subset.copy())
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return ans