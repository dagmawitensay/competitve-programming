# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        if len(arr) <= k:
            return arr
        
        while l <= r:
            a = arr[l]
            b = arr[r]
            if (r - l + 1) == k:
                return arr[l: r + 1]
            elif ((abs(a - x) == abs(b - x)) and a < b) or abs(a - x) < abs(b - x):
                r -= 1
            else:
                l += 1
        
        [1, 2]
        l
        