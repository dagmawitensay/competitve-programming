class Solution: 
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]: 
        seats=[0]*(n+1) 

        for i,j,k in bookings: 
            seats [i-1] += k 
            seats[j] -= k 
        seats.pop() 

        for i in range(1,n): 
            seats[i] += seats[i-1] 

        return seats