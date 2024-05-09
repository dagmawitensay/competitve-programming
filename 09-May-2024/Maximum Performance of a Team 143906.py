# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        joined  = [[e, s] for e, s in zip(efficiency, speed)]
        joined.sort(reverse=True)
        sumVal = 0
        heap = []
        res = 0

        for i in range(len(speed)):
            e, s = joined[i]
            sumVal += s
            res = max(res, (sumVal * e))

            if len(heap) < k - 1:
                heappush(heap, s)
            elif heap and heap[0] < s:
                val = heappop(heap)
                sumVal -= val
                heappush(heap, s)
            else:
                sumVal -= s
        
        return res % MOD