class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        top = sorted(store.items(), key=lambda x:x[1])
        ans = []

        for i in range(len(top) - k, len(top)):
            ans.append(top[i][0])
        
        return ans