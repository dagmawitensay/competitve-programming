class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        max_size = 1
        i, j = 0, 1
        
        while j < n:
            if arr[i] == arr[i + 1]:
                i += 1
                
            while j + 1 < n  and self.isTurbulent(arr, j):
                j += 1
                
            max_size = max(max_size, j - i + 1)
            i = j
            j += 1
        
        return max_size
    
    def isTurbulent(self, arr, j):
        cond1 = arr[j] > arr[j - 1] and arr[j] > arr[j + 1]
        
        cond2 = arr[j] < arr[j + 1] and arr[j] < arr[j - 1]
        
        return cond1 or cond2