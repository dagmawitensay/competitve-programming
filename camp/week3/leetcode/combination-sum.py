class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []

        def backtrack(index):
            if sum(combination) == target:
                ans.append(combination.copy())
                return
            
            if sum(combination) > target or index >= len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    combination.append(candidates[i])
                    backtrack(i)
                    combination.pop()
            
        backtrack(0)
        return ans