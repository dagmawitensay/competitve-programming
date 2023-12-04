class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ""
        
        max_str = ""
        start = 0
        end = 3
        while end < len(num) + 1:
            curr_str = num[start: end]
            if curr_str[0] == curr_str[1] == curr_str[2]:
                if max_str:
                    if int(curr_str[0]) > int(max_str[0]):
                        max_str = curr_str
                else:
                    max_str = curr_str
            
            start += 1
            end += 1
        
        return max_str