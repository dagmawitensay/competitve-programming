# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        joined = [[profit, currCapital] for profit, currCapital in zip(profits, capital)]
        joined.sort(key=lambda x: x[1])

        heap = []
        i = 0

        while k and i < len(profits):
            while i < len(profits) and joined[i][1] <= w:
                heapq.heappush(heap, -joined[i][0])
                i += 1
            
            if heap:
                w += -heapq.heappop(heap)
            k -= 1
        
        while heap and k:
            w += -heapq.heappop(heap)
            k -= 1

        return w
        