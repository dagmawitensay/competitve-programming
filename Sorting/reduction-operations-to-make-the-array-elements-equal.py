class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        visited = 0
        indexes = []
        for i, val in enumerate(nums):
            if val != visited:
                visited = val
                indexes.append(i)
        
        ans = 0
        n = len(nums)
        for i in range(len(indexes) - 1, 0, -1):
            ans += (n - indexes[i])

        return ans
            