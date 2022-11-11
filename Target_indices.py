class Solution(object):
    def targetIndices(self, nums, target):
        target_indices=[]
        sorted=self.selectionSort(nums,len(nums))
        for i in range(len(sorted)):
            if sorted[i]==target:
                target_indices.append(i)
        return target_indices
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
        
