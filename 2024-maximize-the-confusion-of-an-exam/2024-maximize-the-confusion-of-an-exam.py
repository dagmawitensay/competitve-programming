class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counts = {'T': 0, 'F': 0}
        max_nums = 0
        start = 0
        
        for end in range(len(answerKey)):
            counts[answerKey[end]] += 1
            while (end - start + 1) - max(counts.values()) > k:
                counts[answerKey[start]] -= 1
                start += 1
            
            max_nums = max(max_nums, end - start + 1)
        
        return max_nums