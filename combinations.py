"""
LeetCode
77. Combinations
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        soln = []
        def rec(i, acc):
            if len(acc) == k:
                soln.append(list(acc))
                return

            if i > n:
                return

            # Do not choose i
            rec(i+1, acc)
            # Choose i
            acc.append(i)
            rec(i+1, acc)
            acc.pop()

        rec(1, [])
        return soln


def test_1():
    n = 4
    k = 2
    expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert sorted(expected) == sorted(Solution().combine(n, k))


def test_2():
    n = 1
    k = 1
    expected = [[1]]
    assert sorted(expected) == sorted(Solution().combine(n, k))