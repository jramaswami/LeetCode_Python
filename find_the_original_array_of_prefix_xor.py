"""
LeetCode
2433. Find The Original Array of Prefix Xor
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        soln = [0 for _ in pref]
        for i in range(len(pref)-1, 0, -1):
            soln[i] = pref[i] ^ pref[i-1]
        soln[0] = pref[0]
        return soln


def test_3():
    pref = [5,2,0,3,1]
    expected = [5,7,2,3,2]
    assert Solution().findArray(pref) == expected


def test_2():
    pref = [13]
    expected = [13]
    assert Solution().findArray(pref) == expected