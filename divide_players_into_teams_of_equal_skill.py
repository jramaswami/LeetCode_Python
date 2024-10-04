"""
LeetCode
2491. Divide Players Into Teams of Equal Skill
October 2024 Challenge
jramaswami
"""


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        team_skill = skill[left] + skill[right]
        soln = 0
        while left < right:
            if skill[left] + skill[right] != team_skill:
                return -1
            soln += (skill[left] * skill[right])
            left += 1
            right -= 1
        return soln
