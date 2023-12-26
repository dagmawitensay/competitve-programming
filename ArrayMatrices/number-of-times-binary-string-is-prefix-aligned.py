class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_operation = 0
        count = 0

        for i, flip in enumerate(flips):
            max_operation = max(max_operation, flip)
            if i + 1 == max_operation:
                count += 1
        
        return count