# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()

        currTime = 0
        heap = []
        ans = []
        i = 0

        while heap or i < len(tasks):
            if not heap:
                currTime = max(currTime, tasks[i][0])
            
            while i < len(tasks) and tasks[i][0] <= currTime:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            processingTime, index = heapq.heappop(heap)
            currTime += processingTime
            ans.append(index)
            
        return ans