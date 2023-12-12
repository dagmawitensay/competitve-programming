class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in hashMap:
                count = 0
                while num + count in hashMap:
                    count += 1
                
                longest = max(longest, count)
        
        return longest