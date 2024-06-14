# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)

        for a, b in trust:
            graph[a] -= 1
            graph[b] += 1


        for i in range(1, n + 1):
            if graph[i] == n - 1:
                return i

        return -1 
    