class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        target = total - x
        max_len = -1
        currSum = 0
        start = 0
        if total == x:
            return n

        for end in range(n):
            currSum += nums[end]
            while currSum > target and start <= end:
                currSum -= nums[start]
                start += 1
            
            if currSum == target:
                max_len = max(max_len, (end - start + 1))
        
        return -1 if max_len == -1 else n - max_len