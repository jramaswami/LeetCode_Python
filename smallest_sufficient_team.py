"""
LeetCode
1125. Smallest Sufficient Team
July 2023 Challenge
jramaswami
"""


import collections
from typing import List


Person = collections.namedtuple('Person', ['index', 'skill_key'])

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        INF = 1000
        skillset_limit = 1 << len(req_skills)
        skill_lookup = dict((t, i) for i, t in enumerate(req_skills))
        # dp[skill bitset] = min number of people to reach it.
        dp = [(INF,0) for _ in range(skillset_limit)]
        dp[0] = (0, 0)
        for person_index, person_skills in enumerate(people):
            person_bit = 1 << person_index
            # Convert person's skills into a bitset.
            person_skillset = 0
            for skill in person_skills:
                skill_index = skill_lookup[skill]
                person_skillset |= (1 << skill_index)
            # For every possible skillset:
            for skillset in range(skillset_limit - 1, -1, -1):
                skillset0 = skillset | person_skillset
                if dp[skillset0][0] > dp[skillset][0] + 1:
                    dp[skillset0] = (dp[skillset][0] + 1, dp[skillset][1] | person_bit)
        soln = []
        for p in range(len(people)):
            if (1 << p) & dp[skillset_limit-1][1]:
                soln.append(p)
        return soln


def test_1():
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    expected = [0,2]
    assert Solution().smallestSufficientTeam(req_skills, people) == expected


def test_2():
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    expected = [1,2]
    assert Solution().smallestSufficientTeam(req_skills, people) == expected
