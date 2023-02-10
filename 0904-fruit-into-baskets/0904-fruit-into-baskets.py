class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        store = {}
        start = 0
        maxLength = 0
        for end in range(len(fruits)):
            store[fruits[end]] = store.get(fruits[end],0) + 1
            while len(store) > 2:
                store[fruits[start]] -= 1

                if store[fruits[start]] == 0:
                    del store[fruits[start]]
                start += 1
            maxLength = max(maxLength, end - start + 1)
        return maxLength
            