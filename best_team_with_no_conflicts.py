"""
LeetCode
1626. Best Team With No Conflicts
January 2023 Challenge
jramaswami
"""


from typing import *
import functools
import collections


Person = collections.namedtuple('Person', ['age', 'score'])


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        people = [Person(a, s) for s, a in zip(scores, ages)]
        people.sort()

        @functools.cache
        def rec(i,mx):
            if i >= len(people):
                return 0

            # Do not pick this person.
            result = rec(i+1, mx)
            if mx <= people[i].score:
                # If you can, pick this person.
                result = max(
                    result,
                    people[i].score + rec(i+1, max(people[i].score, mx))
                )
            return result

        return rec(0, 0)


def test_1():
    scores = [1,3,5,10,15]
    ages = [1,2,3,4,5]
    expected = 34
    assert Solution().bestTeamScore(scores, ages) == expected


def test_2():
    scores = [4,5,6,5]
    ages = [2,1,2,1]
    expected = 16
    assert Solution().bestTeamScore(scores, ages) == expected


def test_3():
    scores = [1,2,3,5]
    ages = [8,9,10,1]
    expected = 6
    assert Solution().bestTeamScore(scores, ages) == expected
