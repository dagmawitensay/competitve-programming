def checkArithmeticSubarrays(nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer = [None] * len(l)
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            d = temp[1]-temp[0]
            for j in range(len(temp)-1,0,-1):
                print(d,temp[j] - temp[j-1])
                if temp[j] - temp[j-1] != d:
                    answer[i] = False
                    break
                else:
                    answer[i] = True
        return answer
                
        

