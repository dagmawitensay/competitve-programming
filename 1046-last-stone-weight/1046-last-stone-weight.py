class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # To max heap
        stones = list(map(neg, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1 and stones[0] != 0:
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
        
        return -heapq.heappop(stones)