class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums), 2):
            for j in range(nums[i - 1]):
                ans.append(nums[i])
        
        return ans