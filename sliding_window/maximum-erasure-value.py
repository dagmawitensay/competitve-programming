class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniques = set()
        start = 0
        window_sum = 0
        longest = 0

        for end in range(len(nums)):
            while nums[end] in uniques:
                uniques.remove(nums[start])
                window_sum -= nums[start]
                start += 1
            
            window_sum += nums[end]
            uniques.add(nums[end])
            longest = max(longest, window_sum)

        return longest