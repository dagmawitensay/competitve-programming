class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        target = skill[left] + skill[right]
        chemistry = 0
        while left < right:
            if (skill[left] + skill[right]) != target:
                return -1
            else:
                chemistry += skill[left] * skill[right]
                right -= 1
                left += 1

        return chemistry 