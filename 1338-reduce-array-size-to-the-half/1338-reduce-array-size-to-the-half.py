class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = collections.defaultdict(int)
        heap = []

        for num in arr:
            freq[num] += 1

        for key, value in freq.items():
            heapq.heappush(heap, -value)

        setSize = 0
        removed = 0
        half = len(arr) // 2

        while heap and removed < half:
            removed += -heapq.heappop(heap)
            setSize += 1

        return setSize