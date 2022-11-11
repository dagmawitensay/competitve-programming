class Solution:
    def rearrangeArray(self,nums):
        arranged=[0]*len(nums)
        nums.sort()
        j=0
        for i in nums[:(len(nums)-1)//2+1]:
            arranged[j]=i
            j+=2
        j=1
        for i in nums[(len(nums)-1)//2+1:]:
            arranged[j]=i
            j+=2
        return arranged
    
