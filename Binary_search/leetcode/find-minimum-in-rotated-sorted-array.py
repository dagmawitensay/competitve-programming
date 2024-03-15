class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # if nums[low] < nums[high]:
        #     return nums[low]

        # while low <= high:
        #     mid = (low + high) // 2
        #     if mid != 0 and mid != len(nums) - 1 and nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
        #         return nums[mid]
        #     elif nums[mid] > nums[low] and nums[high] > nums[mid]:
        #         return nums[low]
        #     elif nums[mid] > nums[low]:
        #         low = mid
        #     else:
        #         high = mid - 1
        
        # return nums[low + 1] if low + 1 < len(nums) else nums[len(nums) - 1]

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]