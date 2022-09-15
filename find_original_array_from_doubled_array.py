"""
LeetCode :: September 2022 Challenge :: 2007. Find Original Array From Doubled Array
jramaswami
"""


from typing import *
import collections


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freqs = collections.Counter(changed)
        soln = []
        for val in sorted(freqs):
            while freqs[val]:
                # Add val to solution.
                soln.append(val)
                # Remove the current value.
                freqs[val] -= 1
                # Find its match.
                if freqs[val * 2] == 0:
                    return []
                freqs[val * 2] -= 1
        return soln


def test_1():
    changed = [1,3,4,2,6,8]
    expected = [1,3,4]
    assert Solution().findOriginalArray(changed) == expected


def test_2():
    changed = [6,3,0,1]
    expected = []
    assert Solution().findOriginalArray(changed) == expected


def test_3():
    changed = [1]
    expected = []
    assert Solution().findOriginalArray(changed) == expected


def test_4():
    "WA"
    changed = [0,0,0,0]
    expected = [0, 0]
    assert Solution().findOriginalArray(changed) == expected