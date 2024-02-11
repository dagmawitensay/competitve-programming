class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counts = Counter(nums)
        subarray_count = defaultdict(lambda: 0)
        start = 0
        subarrays = 0

        for end in range(len(nums)):
            subarray_count[nums[end]] += 1
            while len(subarray_count) == len(counts):
                subarrays += (len(nums) - end)
                subarray_count[nums[start]] -= 1
                if subarray_count[nums[start]] == 0:
                    del subarray_count[nums[start]]
                
                start += 1
        
        return subarrays