class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    #     ans = []
    #     curr = []

    #     def backtrack(index):
    #         if len(curr) == k:
    #             ans.append(curr.copy())
    #             return
            
    #         for path in range(index + 1, n + 1):
    #             curr.append(path)
    #             backtrack(path)
    #             curr.pop()
            
    #     backtrack(0)

    #     return ans
        nums = [i for i in range(1, n + 1)]
        ans = []
        
        def backtrack(index, curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            
            if index >= n:
                return
            if len(curr) > k:
                return
            
            curr.append(nums[index])
            backtrack(index + 1, curr)
            curr.pop()
            backtrack(index + 1, curr)
        
        backtrack(0, [])
        return ans