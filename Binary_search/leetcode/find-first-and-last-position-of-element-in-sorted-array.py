class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left, right, flag):
            low, high = left, right
            pos = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    pos = mid
                    if flag:
                        high = mid - 1
                    else:
                        low = mid + 1
                
            return pos
        
        leftStart = binarySearch(0, len(nums) - 1, True)
        rightEnd = binarySearch(0, len(nums) - 1, False)
    
        return [leftStart, rightEnd]