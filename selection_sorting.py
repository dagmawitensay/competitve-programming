class Solution: 
    def select(self, arr, i):
        minimum = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        
        return minimum
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minimum = self.select(arr, i)
            arr[i], arr[minimum]  = arr[minimum], arr[i]
