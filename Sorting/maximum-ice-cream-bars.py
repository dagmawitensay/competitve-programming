class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        min_val = min(costs)
        if coins < min_val:
            return 0

        arr = [0] * (max_val + 1)
        for val in costs:
            arr[val] += 1
        
        j = 0
        for i in range(len(arr)):
            while arr[i] != 0:
                costs[j] = i
                arr[i] -= 1
                j += 1
        
        i = 0
        print(costs)
        while coins > 0 and i < len(costs) and costs[i] <= coins:
            coins -= costs[i]
            i += 1
        
        return i 
