class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        visited = 0
        ans = 0
        n = len(nums)
        for i, val in enumerate(nums):
            if val != visited:
                visited = val
                if i != 0:
                    ans += (n - i)

        return ans
            