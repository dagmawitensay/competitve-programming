# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller_arr = [0] * len(nums)
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            l, r = 0, 0
            while l < len(left) or r < len(right):
                if r >= len(right) or (l < len(left) and left[l][1] <= right[r][1]):
                    result.append(left[l])
                    smaller_arr[left[l][0]] += r
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            return result

        merge_sort(list(enumerate(nums)))
        return smaller_arr