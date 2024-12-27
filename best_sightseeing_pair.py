"""
LeetCode
1014. Best Sightseeing Pair
December 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        I, V = 1, 2
        soln = 0
        max_item = None
        for j, n in enumerate(values):
            if max_item:
                soln = max(soln, n + max_item[V] + max_item[I] - j)
            item = (n+j, j, n)
            max_item = max(max_item, item) if max_item else item
        return soln



def test_1():
    values = [8,1,5,2,6]
    expected = 11
    assert Solution().maxScoreSightseeingPair(values) == expected


def test_2():
    values = [1,2]
    expected = 2
    assert Solution().maxScoreSightseeingPair(values) == expected
