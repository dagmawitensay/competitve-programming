class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # subset = []
        # visited = set()
        # def backtrack(index):
        #     if tuple(subset) not in visited:
        #         visited.add(tuple(subset))
        #         ans.append(subset.copy())
     
        #     if index >= len(nums):
        #         return
            
        #     subset.append(nums[index])
        #     backtrack(index + 1)
        #     subset.pop()
        #     backtrack(index + 1)

        # backtrack(0)
        # return ans
        ans = []
        subset = []

        def backtrack(index):
            ans.append(subset.copy())
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return ans