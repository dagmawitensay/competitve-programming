class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        uniques = {}
        start = 0
        max_fruits = 0

        for end in range(len(fruits)):
            uniques[fruits[end]] = uniques.get(fruits[end], 0) + 1
            while len(uniques) > 2:
                uniques[fruits[start]] -= 1
                if uniques[fruits[start]] == 0:
                    del uniques[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits