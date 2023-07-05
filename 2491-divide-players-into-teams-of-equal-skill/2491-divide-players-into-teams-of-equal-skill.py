class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() 
        i = 0
        j = len(skill) - 1
        target = skill[0] + skill[-1]
        groups = []
        chemistry = 0
        
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            groups.append([skill[i], skill[j]])
            i += 1
            j -= 1
        
        for group in groups:
            chemistry += (group[0] * group[1])
        
        return chemistry
        