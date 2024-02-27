class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr = []
        
        def backtrack():
            if len(curr) == len(nums):
                permutations.append(curr.copy())
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack()
                    curr.pop()
            
        backtrack()
        return permutations