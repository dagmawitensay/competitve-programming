class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        windowSize = 2 * k + 1
        windowSum = 0
        n = len(nums)
        result = [-1] * n
        if windowSize > n:
            return result

        for end in range(n):
            windowSum += nums[end]

            if end - windowSize >= 0:
                windowSum -= nums[end - windowSize]
            
            if end >= windowSize - 1:
                result[end - k] = windowSum // windowSize
        
        return result