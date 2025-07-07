"""
LeetCode
1353. Maximum Number of Events That Can Be Attended
July 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/1353
"""


import math
import collections
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        event_dict = collections.defaultdict(list)
        earliest_start, latest_end = math.inf, 0

        for start, end in events:
            event_dict[start].append(end)
            earliest_start = min(earliest_start, start)
            latest_end = max(latest_end, end)

        min_heap = []
        max_events_attended = 0

        for day in range(earliest_start, latest_end + 1):
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            for end in event_dict[day]:
                heapq.heappush(min_heap, end)

            if min_heap:
                max_events_attended += 1
                heapq.heappop(min_heap)

        return max_events_attended



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