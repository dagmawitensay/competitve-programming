class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        total = sum(map(int, s))
        prefix_sum = 0

        for i in range(len(s) - 1):
            prefix_sum += int(s[i])
            curr_score = (i + 1 - prefix_sum) + (total - prefix_sum)
            max_score = max(max_score, curr_score)
        
        return max_score