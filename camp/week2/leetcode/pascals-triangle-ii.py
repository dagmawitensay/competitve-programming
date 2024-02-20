class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(arr, index):
            if index == 0:
                return arr
            
            new_arr = [1]
            for i in range(1, len(arr)):
                new_arr.append(arr[i - 1] + arr[i])
            
            new_arr.append(1)

            return helper(new_arr, index - 1)
        
        return helper([1], rowIndex)