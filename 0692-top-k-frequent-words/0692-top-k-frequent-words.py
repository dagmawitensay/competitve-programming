class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = {}
        for word in words:
            store[word] = store.get(word, 0) + 1
        
        print(store)
        sorted_map = sorted(store.items(), key=lambda x: (-x[1], x[0]))
        ans = [sorted_map[i][0] for i in range(k)]
        
        return ans