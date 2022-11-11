def smallerNumbersThanCurrent(nums):
        result=[]
        ctr=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    ctr+=1
            result.append(ctr)
            ctr=0
        return result


        