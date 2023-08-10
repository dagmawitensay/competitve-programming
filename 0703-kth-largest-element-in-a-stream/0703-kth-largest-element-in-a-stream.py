class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = []
        self.k = k
        for i in nums:
            self.add(i)
    
    def add(self, val: int) -> int:
        if len(self.store) < self.k:
            heapq.heappush(self.store, val)
        elif self.store[0] < val:
            heapq.heappop(self.store)
            heapq.heappush(self.store, val)
        
        return self.store[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)