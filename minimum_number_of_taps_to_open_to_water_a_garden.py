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
        # We do not care if a tap extends outside of the garden, so limit the
        # ranges to the garden
        taps = [Tap(max(i-k, 0), min(i+k, n)) for i, k in enumerate(ranges)]
        taps.sort(key=operator.attrgetter('right'))

        open_taps = [Tap(0,0)]
        for tap in taps:
            # Does this tap overlap with the current range and extend it?
            if tap.left <= open_taps[-1].right and tap.right > open_taps[-1].right:
                # Invariant current tap starts to the right of anything in the
                # open taps because the taps were sorted by right
                while open_taps and tap.left <= open_taps[-1].left:
                    open_taps.pop()
                # Only count the extension
                if open_taps:
                    open_taps.append(Tap(open_taps[-1].right, tap.right))
                else:
                    open_taps.append(tap)

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
    "WA"
    n = 8
    ranges = [4,0,0,0,4,0,0,0,4]
    expected = 1
    assert Solution().minTaps(n, ranges) == expected


def test_4():
    "WA"
    n = 9
    ranges = [0,5,0,3,3,3,1,4,0,4]
    expected = 2
    assert Solution().minTaps(n, ranges) == expected


def test_5():
    "WA"
    n = 7
    ranges = [1,2,1,0,2,1,0,1]
    expected = 3
    assert Solution().minTaps(n, ranges) == expected