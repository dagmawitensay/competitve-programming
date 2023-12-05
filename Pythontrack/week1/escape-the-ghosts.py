class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_distance = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(target[0] - x) + abs(target[1] - y) <= target_distance:
                return False
        
        return True