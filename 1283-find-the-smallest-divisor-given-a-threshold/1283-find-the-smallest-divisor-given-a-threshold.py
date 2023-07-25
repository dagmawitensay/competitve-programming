class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(curr_num):
            return sum([ceil(i / curr_num) for i in nums])
        
        l, r = 1, max(nums)
        
        while l < r:
            mid = (l + r) // 2
            check = helper(mid)
            if check > threshold:
                l = mid + 1
            else:
                r = mid
        
        return l