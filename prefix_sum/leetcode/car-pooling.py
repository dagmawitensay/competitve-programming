class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sits = [0] * 1001
        for n, f, t in trips:
            sits[f] += n
            sits[t] -= n
        
        total_passangers = 0
        for i in sits:
            total_passangers += i
            if total_passangers > capacity:
                return False
        
        return True