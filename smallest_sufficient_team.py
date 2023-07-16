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
        # Create a lookup to see which people fulfill a given skill.
        skill_lookup = dict((t, i) for i, t in enumerate(req_skills))

        def add_skill(curr_skills, skill_index):
            return curr_skills | (1 << skill_index)


        def make_skill_key(person_skills):
            key = 0
            for skill in person_skills:
                skill_index = skill_lookup[skill]
                key = add_skill(key, skill_index)
            return key

        persons = [Person(i, make_skill_key(p)) for i, p in enumerate(people)]
        person_skill_lookup = [[] for _ in req_skills]
        key_limit = 1 << (len(req_skills))
        for skill_index, _ in enumerate(req_skills):
            skill_bit = 1 << skill_index
            for person in persons:
                if skill_bit & person.skill_key:
                    person_skill_lookup[skill_index].append(person)

        # Recursive solution.
        def rec(skill_index, curr_skill_key, curr_people_indexes):
            # Base cases
            if curr_skill_key == (key_limit - 1):
                return list(curr_people_indexes)

            if skill_index >= len(req_skills):
                return None

            # If the current skill is not fulfilled, try each person
            # that can fulfill the skill.
            result = None
            if curr_skill_key & (1 << skill_index) == 0:
                for person in person_skill_lookup[skill_index]:
                    curr_people_indexes.append(person.index)
                    local_result = rec(
                        skill_index + 1,
                        curr_skill_key | person.skill_key,
                        curr_people_indexes
                    )
                    curr_people_indexes.pop()
                    if local_result:
                        if not result or len(result) > len(local_result):
                            result = local_result
                return result

            # If curent skill is fulfilled, move on to next skill.
            return rec(skill_index + 1, curr_skill_key, curr_people_indexes)

        return rec(0, 0, [])


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
