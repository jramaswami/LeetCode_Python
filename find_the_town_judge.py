"""
LeetCode :: January 2022 Challenge :: 997. Find the Town Judge
jramaswami
"""


class Solution:

    def findJudge(self, n, trust):
        trusts_another = [0 for _ in range(n)]
        trusted_by_another = [0 for _ in range(n)]

        for a, b in trust:
            trusts_another[a-1] += 1
            trusted_by_another[b-1] += 1

        paranoid = set(i for i, t in enumerate(trusts_another) if t == 0)
        trustworthy = set(i for i, t in enumerate(trusted_by_another) if t == n - 1)

        maybe_judge = paranoid & trustworthy
        if len(maybe_judge) == 1:
            return 1 + maybe_judge.pop()
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
