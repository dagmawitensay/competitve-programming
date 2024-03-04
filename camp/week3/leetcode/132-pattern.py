class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minVal = nums[0]

        for num in nums:
            if not stack or stack[-1][0] > num:
                stack.append((minVal, num))
            else:
                while stack and stack[-1][1] < num:
                    stack.pop()
                
                if stack and stack[-1][1] > num and stack[-1][0] < num:
                    return True
                
                stack.append((minVal, num))
               
            minVal = min(minVal, num)
        
        return False