"""
LeetCode :: March 2022 Challenge :: 881. Boats to Save People
jramaswami
"""


import collections


class Solution:
    def numRescueBoats(self, people, limit):
        people0 = collections.deque(sorted(people))
        soln = 0
        while people0:
            if len(people0) > 1 and people0[0] + people0[-1] <= limit:
                people0.popleft()
            people0.pop()
            soln += 1
        return soln


def test_1():
    people = [1,2]
    limit = 3
    expected = 1
    assert Solution().numRescueBoats(people, limit) == expected


def test_2():
    people = [3,2,2,1]
    limit = 3
    expected = 3
    assert Solution().numRescueBoats(people, limit) == expected


def test_3():
    people = [3,5,3,4]
    limit = 5
    expected = 4
    assert Solution().numRescueBoats(people, limit) == expected


def test_4():
    "RTE"
    people = [2,4]
    limit = 5
    expected = 2
    assert Solution().numRescueBoats(people, limit) == expected
