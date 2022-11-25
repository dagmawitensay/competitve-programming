def largestNumber(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for j in range(len(nums)):
            for i in range(len(nums)-1):
                first = str(nums[i])+str(nums[i+1])
                second = str(nums[i+1])+str(nums[i])
                if second > first:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        largest = ""
        zero_ctr = 0
        for number in nums:
            if number == 0:
                zero_ctr +=1 
            largest += str(number)
        if zero_ctr == len(nums):
            largest = "0"
        return largest