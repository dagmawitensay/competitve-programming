class Solution:
    def rearrangeArray(self,nums):
        arranged=[0]*len(nums)
        self.mergeSort(nums)
        j=0
        for i in nums[:(len(nums)-1)//2+1]:
            arranged[j]=i
            j+=2
        j=1
        for i in nums[(len(nums)-1)//2+1:]:
            arranged[j]=i
            j+=2
        return arranged
    def mergeSort(self,list): 
        if len(list) > 1: 
            firstHalf = list[ : len(list) // 2] 
            self.mergeSort(firstHalf) 
            
            secondHalf = list[len(list) // 2 : ] 
            self.mergeSort(secondHalf) 
            
            self.merge(firstHalf, secondHalf, list) 
    def merge(self,list1, list2, temp): 
            current1 = 0 
            current2 = 0 
            current3 = 0 
            
            while current1 < len(list1) and current2 < len(list2): 
                if list1[current1] < list2[current2]: 
                    temp[current3] = list1[current1] 
                    current1 += 1
                    current3 += 1
                else: 
                    temp[current3] = list2[current2] 
                    current2 += 1
                    current3 += 1 
            while current1 < len(list1): 
                temp[current3] = list1[current1] 
                current1 += 1
                current3 += 1
                
            while current2 < len(list2): 
                temp[current3] = list2[current2] 
                current2 += 1
                current3 += 1

