class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n, m = len(processorTime), len(tasks)
        processorTime.sort()
        tasks.sort(reverse=True)
        j = 0
        total, curr_max = 0, 0

        for i in range(0, m, m // n):
            total = max(total, tasks[i] + processorTime[j])
            j += 1

        
        return total


