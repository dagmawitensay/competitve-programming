# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_handle(mid):
            count = 1
            prev_pos = position[0]

            for curr_pos in position[1:]:
                if curr_pos - prev_pos >= mid:
                    count += 1
                    prev_pos = curr_pos

            return count >= m 


        l, r =  1, position[-1] - position[0]

        while l < r:
            mid = (l + r + 1) // 2
            if can_handle(mid):
                l = mid
            else:
                r = mid -1
        

        return l
    
                
                

            