"""
LeetCode
1326. Minimum Number of Taps to Open to Water a Garden
August 2023 Challenge
jramaswami
"""


import collections
import operator
from typing import List


Tap = collections.namedtuple('Tap', ['left', 'right'])


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = [Tap(i-k, i+k) for i, k in enumerate(ranges)]
        taps.sort(key=operator.attrgetter('right'))

        open_taps = [Tap(0,0)]
        for tap in taps:
            # Does this tap overlap with the current range and extend it?
            if tap.left <= open_taps[-1].right and tap.right > open_taps[-1].right:
                # Invariant current tap starts to the right of anything in the
                # open taps because the taps were sorted by right
                while open_taps and tap.left <= open_taps[-1].left:
                    open_taps.pop()
                open_taps.append(tap)
        print(taps)
        print(open_taps)
        if open_taps[-1].right >= n:
            return len(open_taps)
        return -1


def test_1():
    n = 5
    ranges = [3,4,1,1,0,0]
    expected = 1
    assert Solution().minTaps(n, ranges) == expected


def test_2():
    n = 3
    ranges = [0,0,0,0]
    expected = -1
    assert Solution().minTaps(n, ranges) == expected


def test_3():
    n = 8
    ranges = [4,0,0,0,4,0,0,0,4]
    expected = 1
    assert Solution().minTaps(n, ranges) == expected