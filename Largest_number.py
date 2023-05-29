class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]

        if not nums:
            return ""
        
        if len(nums) == 1:
            return str(nums[0])
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif y + x > x + y:
                return 1
            else:
                return 0

        nums = sorted(nums, key=cmp_to_key(compare))
        
        return str(int("".join(nums)))
