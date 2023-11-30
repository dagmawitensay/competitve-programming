class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr = 0
        indexes=len(nums)
        for i in range(indexes):
            for j in range(i,indexes):
                if nums[i]==nums[j] and i <j:
                    ctr+=1
        return ctr
    