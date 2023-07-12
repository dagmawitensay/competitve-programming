class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sums = [nums[0]]
        for i in range(1, len(nums)):
            self.pref_sums.append(self.pref_sums[i - 1] + nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.pref_sums[right]
        return self.pref_sums[right] - self.pref_sums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)