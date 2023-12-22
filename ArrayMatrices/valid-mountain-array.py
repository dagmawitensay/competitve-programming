class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_index = arr.index(max(arr))
        if len(arr) < 3 or max_index == 0 or max_index == len(arr) - 1:
            return False

        for i in range(1, max_index + 1):
            if arr[i - 1] >= arr[i]:
                return False
        
        for i in range(len(arr) - 1, max_index, -1):
            if arr[i - 1] <= arr[i]:
                print(arr[i - 1], arr[i])
                return False
        
        return True