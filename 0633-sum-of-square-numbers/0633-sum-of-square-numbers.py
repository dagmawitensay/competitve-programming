class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        options = [x for x in range(int(sqrt(c)) + 1)]
        beg = 0
        end = len(options) - 1
        while beg <= end:
            square_sum = options[beg] ** 2 + options[end] ** 2
            if square_sum == c:
                return True
            
            if square_sum > c:
                end -= 1
            else:
                beg += 1
       
        return False
        