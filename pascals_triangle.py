"""
LeetCode :: June 2021 Challenge :: Pascal's Triangle
jramaswami
"""


class Solution:
    def generate(self, num_rows):
        P = [[1], [1, 1]]
        while len(P) < num_rows:
            row = [1]
            for a, b in zip(P[-1][:-1], P[-1][1:]):
                row.append(a + b)
            row.append(1)
            P.append(row)

        return P[:num_rows]


def test_1():
    expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert Solution().generate(5) == expected


def test_2():
    expected = [[1]]
    assert Solution().generate(1) == expected