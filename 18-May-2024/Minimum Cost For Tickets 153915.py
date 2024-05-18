# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(index, covered):
            if index == len(days):
                return 0
            
            if days[index] > covered:
                return min(costs[0] + dp(index + 1, days[index]), costs[1] + dp(index + 1, days[index] + 6), costs[2] + dp(index + 1, days[index] + 29))
            else:
                return dp(index + 1, covered)
        
        return dp(0, 0)
            