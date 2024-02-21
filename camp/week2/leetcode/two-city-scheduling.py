class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for i, cost in enumerate(costs):
            diffs.append([cost[0] - cost[1], i])
        
        diffs.sort()
        total = 0 

        for i in range(len(diffs)):
            if i >= (len(diffs) // 2):
                total += costs[diffs[i][1]][1]
            else:
                total += costs[diffs[i][1]][0]
        
        return total