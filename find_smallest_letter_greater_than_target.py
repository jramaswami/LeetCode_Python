"""
LeetCode
744. Find Smallest Letter Greater Than Target
June 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Variation on binary search.
        lo = 0
        hi = len(letters) - 1
        soln = len(letters)
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if letters[mid] <= target:
                lo = mid + 1
            else:
                soln = min(soln, mid)
                hi = mid - 1

        if soln == len(letters):
            return letters[0]
        return letters[soln]



def test_1():
    letters = ["c","f","j"]
    target = "a"
    expected = "c"
    assert Solution().nextGreatestLetter(letters, target) == expected


def test_2():
    letters = ["c","f","j"]
    target = "c"
    expected = "f"
    assert Solution().nextGreatestLetter(letters, target) == expected


def test_3():
    letters = ["x","x","y","y"]
    target = "z"
    expected = "x"
    assert Solution().nextGreatestLetter(letters, target) == expected