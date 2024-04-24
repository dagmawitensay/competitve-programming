# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indeegre = [0] * numCourses
        graph = defaultdict(list)
        queue = deque([])
        dependent = defaultdict(set)

        for s, d in prerequisites:
            graph[s].append(d)
            indeegre[d] += 1
        
        for i in range(len(indeegre)):
            if indeegre[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()

            for neighbor in graph[course]:
                dependent[neighbor].add(course)
                dependent[neighbor].update(dependent[course])
                indeegre[neighbor] -= 1
                if indeegre[neighbor] == 0:
                    queue.append(neighbor)
        
        res = []
        for s, d in queries:
            if s in dependent[d]:
                res.append(True)
            else:
                res.append(False)

        return res