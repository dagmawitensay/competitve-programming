class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        front_back = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in front_back:
                front_back.remove(fronts[i])
        
        return min(front_back) if len(front_back) != 0 else 0