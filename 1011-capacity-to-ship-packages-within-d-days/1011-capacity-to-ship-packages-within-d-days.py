class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = max(weights)

        while left < right:
            mid = left + (right - left) // 2
            print("mid", mid)
            if self.canSheep(mid, weights, days):
                right = mid
            else:
                left = mid + 1
        
        print(left, right)
        
        return left
    

    def canSheep(self, capacity, weights, days):
        curr_sum = 0
        test_days = 0
        for weight in weights:
            if curr_sum + weight > capacity:
                days += 1
                curr_sum = 0
                curr_sum += weight
        
        if test_days > days:
            return False
        
        return True