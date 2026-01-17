"""
LeetCode
3047. Find the Largest Area of Square Inside Two Rectangles
January 2026 Challenge
jramaswami
"""


import collections
import itertools
from typing import List, Tuple


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def overlap(i: int, j: int) -> Tuple[int, int]:
            """Return horizontal and vertical overlaps between
            rectangles given the indexes i, j.
            """
            i_left, i_bottom = bottomLeft[i]
            i_right, i_top = topRight[i]
            j_left, j_bottom = bottomLeft[j]
            j_right, j_top = topRight[j]
            # i above j
            if i_bottom >= j_top:
                return 0, 0
            # i below j
            if i_top <= j_bottom:
                return 0, 0
            # i left of j
            if i_right <= j_left:
                return 0, 0
            # i right of j
            if i_left >= j_right:
                return 0, 0
            # Which rectangle is most left?
            if i_left <= j_left:
                # i is left, so j left must be between i left & right
                assert i_left <= j_left <= i_right
                horizontal_overlap = min(i_right, j_right) - j_left
            else:
                # j is left, so i left must be between j left & right
                assert j_left <= i_left <= j_right
                horizontal_overlap = min(i_right, j_right) - i_left
            # Which rectangle is on bottom?
            if i_bottom <= j_bottom:
                # i is bottom, so j bottom must be between i bottom & top
                assert i_bottom <= j_bottom <= i_top
                vertical_overlap = min(i_top, j_top) - j_bottom
            else:
                # j is bottom, so i bottom must be between j bottom & top
                assert j_bottom <= i_bottom <= j_top
                vertical_overlap = min(i_top, j_top) - i_bottom
            return horizontal_overlap, vertical_overlap

        soln = 0
        # Line sweep
        # events[x] = event
        # event = (event type, rectangle index)
        events = collections.defaultdict(list)
        START, END = 1, 0
        for i, (x, _) in enumerate(bottomLeft):
            events[x].append((START, i))
        for i, (x, _) in enumerate(topRight):
            events[x].append((END, i))
        
        active = set()
        for x in sorted(events):
            for t, i in events[x]:
                if t == START:
                    active.add(i)
                else:
                    active.remove(i)
            for i, j in itertools.combinations(active, 2):
                h, v = overlap(i, j)
                dim = min(h, v)
                soln = max(soln, (dim * dim))
        return soln


def test_1():
    bottomLeft = [[1,1],[2,2],[3,1]]
    topRight = [[3,3],[4,4],[6,6]]
    expected = 1
    assert Solution().largestSquareArea(bottomLeft, topRight) == expected
