from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counted = Counter(words)

        heap = [(-count, word) for word, count in counted.items()]
        heapq.heapify(heap)

        ans = []
        for i in range(k):
            count, word = heapq.heappop(heap)
            ans.append(word)
        
        return ans