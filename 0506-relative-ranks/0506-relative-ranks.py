class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = [(val, i) for i, val in enumerate(score)]
        temp.sort(reverse=True)
        ans = [0] * len(temp)
        
        for i, vals in enumerate(temp):
            if i == 0:
                ans[vals[1]] = 'Gold Medal'
            elif i == 1:
                ans[vals[1]] = 'Silver Medal'
            elif i == 2:
                ans[vals[1]] = 'Bronze Medal'
            else:
                ans[vals[1]] = str(i + 1)
        
        return ans
        