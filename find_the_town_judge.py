"""
LeetCode
997. Find the Town Judge
January 2023 Challenge
jramaswami
"""


class Solution:

    def findJudge(self, n, trust):
        trusts = [0 for _ in range(n)]
        is_trusted_by = [0 for _ in range(n)]

        for a, b in trust:
            # a trusts b
            trusts[a-1] += 1
            is_trusted_by[b-1] += 1

        for i in range(n):
            if trusts[i] == 0 and is_trusted_by[i] == n-1:
                return i+1
        return -1


def test_1():
    n = 2
    trust = [[1,2]]
    assert Solution().findJudge(n, trust) == 2


def test_2():
    n = 3
    trust = [[1,3],[2,3]]
    assert Solution().findJudge(n, trust) == 3


def test_3():
    n = 3
    trust = [[1,3],[2,3],[3,1]]
    assert Solution().findJudge(n, trust) == -1
