class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        store = []
        ans = set()

        for i, v in enumerate(list1):
            dict1[v] = i
        
        for i, v in enumerate(list2):
            if v in dict1:
                store.append((v, i + dict1[v]))
        
        store.sort(key=lambda x:x[1])

        ans.add(store[0][0])
        for i in range(1, len(store)):
            if store[i][1] == store[i - 1][1] and store[i] not in ans:
                ans.add(store[i - 1][0])
                ans.add(store[i][0])
            else:
                break
        
        return list(ans)