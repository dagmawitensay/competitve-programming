class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        combination = []
        def backtrack(num):
            combSum = sum(combination)
            if len(combination) == k:
                if combSum == n:
                    ans.append(combination.copy())
                return
            
            if num > 9 or combSum > n:
                return
            
            for val in range(num, 10):
                if n - val > 0:
                    combination.append(val)
                    backtrack(val + 1)
                    combination.pop()
        
        backtrack(1)
        return ans