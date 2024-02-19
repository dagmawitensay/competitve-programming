class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        j = 0

        while tickets[k] != 0:
            if tickets[j] != 0:
                tickets[j] -= 1
                time += 1
            
            j += 1
            
            if j == len(tickets):
                j = 0
        
        return time
        

            
