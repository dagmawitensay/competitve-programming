# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = [0] * n

        for prevCourse, nextCourse in relations:
            graph[prevCourse - 1].append(nextCourse - 1)
            indegree[nextCourse - 1] += 1


        queue = deque()
        requiredTimes = [0] * n

        for node, val in enumerate(indegree):
            if val == 0:
                queue.append(node)
                requiredTimes[node] = time[node]
        

        while queue:
            node = queue.popleft()

            for nbr in graph[node]:
                requiredTimes[nbr] = max(requiredTimes[nbr] , requiredTimes[node] + time[nbr])
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return max(requiredTimes)

         