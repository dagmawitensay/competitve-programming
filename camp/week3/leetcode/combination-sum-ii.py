class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        candidates.sort()

        def backtrack(index):
            combSum = sum(combination)
            if combSum == target:
                ans.append(combination.copy())
                return
            
            if combSum > target or index >= len(candidates):
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] >= 0:
                    combination.append(candidates[i])
                    backtrack(i + 1)
                    combination.pop()
            
        backtrack(0)

        return ans