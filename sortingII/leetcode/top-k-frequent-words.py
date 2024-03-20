class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = list(Counter(words).items())
        counts.sort(key=lambda x: (-x[1], x[0]))
        print(counts)
        res = [key for key, val in counts[:k]]

        return res