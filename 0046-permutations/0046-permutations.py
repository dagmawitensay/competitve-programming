class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        
        def backtrack(current):
            if len(current) == n:
                permutations.append(current[:])
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
        
        backtrack([])
        
        return permutations
    