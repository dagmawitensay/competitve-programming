class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        windowSum = sum(cardPoints[:n - k])
        ans = total_sum - windowSum

        for i in range(k):
            windowSum -= cardPoints[i]
            windowSum += cardPoints[i + n - k]
            ans = max(ans, total_sum - windowSum)

        return ans