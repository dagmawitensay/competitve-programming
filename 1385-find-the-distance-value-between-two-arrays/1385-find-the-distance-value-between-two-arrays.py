class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0

        for num in arr1:
            if self.checkDistance(num, arr2, d):
                count += 1
        
        return count

    
    def checkDistance(self, val, arr2, d):
        low = 0
        high = len(arr2) - 1

        while low <= high:
            mid = low + (high - low) // 2
            diff = abs(val - arr2[mid])
            if diff <= d:
                return False
            else:
                low = mid + 1

        return True

    