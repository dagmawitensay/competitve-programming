# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = dict()

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
            
            indegree[recipes[i]] = len(ingredients[i])

        queue = deque([*supplies])
        res = []

        while queue:
            node = queue.popleft()

            for nbr in graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    res.append(nbr)
            
        return res
        
