class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pas = [0]*1001
        
        for a, s, e in trips:
            pas[s] += a
            pas[e] -= a
        trip_passangers = 0
        for n in pas:
            trip_passangers += n
            if trip_passangers > capacity:
                return False
        return True