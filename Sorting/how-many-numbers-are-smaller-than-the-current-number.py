class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        counts = {}
        for i, num in enumerate(nums_sorted):
            if num not in counts:
                counts[num] = i

        ans = []
        for num in nums:
            ans.append(counts[num])
        
        return ans