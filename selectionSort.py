class Solution: 
    def select(self, arr, i):
        min=arr[i]
        position=i
        for j in range(i+1,len(arr)):
            if min>arr[j]:
                min=arr[j]
                position=j
        return position
    def selectionSort(self, arr,n):
        for i in range(n):
            selected=self.select(arr,i)
            arr[i],arr[selected]=arr[selected],arr[i]
        return arr
    


