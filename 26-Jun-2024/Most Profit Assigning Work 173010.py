# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (right + left) // 2
                if arr[mid][0] > target:
                    right = mid - 1
                elif arr[mid][0] < target:
                    left = mid + 1
                else:
                    return mid
            
            return left

        joined = []
        
        for level, val in zip(difficulty, profit):
            joined.append([level, val])

        joined.sort(key=lambda x: (x[0], -x[1]))

        for i in range(1, len(joined)):
            joined[i][1] = max(joined[i][1], joined[i - 1][1])

        worker.sort()
        totalProfit = 0

        for val in worker:
            index = binary_search(joined, val)
            if index < len(joined) and joined[index][0] == val:
                totalProfit += joined[index][1]
            elif index - 1 >= 0:
                totalProfit += joined[index - 1][1]

        return totalProfit