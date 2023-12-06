class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less = []
        greater = []
        equals = 0

        for i in range(n):
            if nums[i] > pivot:
                greater.append(nums[i])
            elif nums[i] == pivot:
                equals += 1
            else:
                less.append(nums[i])
        
        return less + [pivot] * equals + greater