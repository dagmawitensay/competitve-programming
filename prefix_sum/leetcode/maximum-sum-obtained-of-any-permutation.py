class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freqs = [0] * (len(nums) + 1)
        
        for start, end in requests:
            freqs[start] += 1
            freqs[end + 1] -= 1
        
        for i in range(1, len(nums)):
            freqs[i] += freqs[i - 1]
        
        freqs.sort()
        nums.sort()

        result = 0
        for i in range(len(nums)):
            result +=  nums[i] * freqs[i + 1]
        
        return result % (10 ** 9 + 7)