"""
LeetCode
1353. Maximum Number of Events That Can Be Attended
July 2025 Challenge
jramaswami
"""

import collections
from typing import List


Event = collections.namedtuple('Event', ['start', 'end'])


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events0 = [Event(*e) for e in events]
        events0.sort()
        timer = -1
        soln = 0
        for event in events0:
            if timer <= event.end:
                timer = event.start + 1
                soln += 1
        return soln


def test_1():
    events = [[1,2],[2,3],[3,4]]
    expected = 3
    assert Solution().maxEvents(events) == expected


def test_2():
    events = [[1,2],[2,3],[3,4],[1,2]]
    expected = 4
    assert Solution().maxEvents(events) == expected


def test_3():
    "WA"
    events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    expected = 4
    assert Solution().maxEvents(events) == expected