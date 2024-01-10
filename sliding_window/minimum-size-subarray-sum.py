class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = float('inf')
        start = 0
        window_sum = 0

        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                smallest = min(smallest, end - start + 1)
                window_sum -= nums[start]
                start += 1
        
        return smallest if smallest != float('inf') else 0