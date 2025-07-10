"""
LeetCode
3440. Reschedule Meetings for Maximum Free Time II
July 2025 Challenge
jramaswami
"""


import collections
from typing import List


Meeting = collections.namedtuple('Meeting', ['start', 'end', 'duration', 'index'])
Gap = collections.namedtuple('Gap', ['preceding', 'following', 'duration'])


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        meetings = [Meeting(0, 0, 0, 0)]
        meetings.extend(Meeting(s, e, e-s, i+1) for i, (s, e), in enumerate(zip(startTime, endTime)))
        meetings.append(Meeting(eventTime, eventTime, 0, len(meetings)))
        meetings.sort()
        gaps = [Gap(a.index, b.index, b.start - a.end) for a, b in zip(meetings[:-1], meetings[1:])]
        soln = max(g.duration for g in gaps)

        INF = pow(10,10)
        for meeting in meetings[1:-1]:
            smallest_gap = Gap(None, None, INF)
            my_gap = meetings[meeting.index+1].start - meetings[meeting.index-1].end
            # Find the smallest gap that any meeting will fit it
            for gap in gaps:
                if gap.preceding == meeting.index or gap.following == meeting.index:
                    # This is where the meeting currently resides'
                    # What is the gap if this meeting is moved left/right
                    soln = max(soln, my_gap - meeting.duration)
                else:
                    if meeting.duration <= gap.duration:
                        if gap.duration < smallest_gap.duration:
                            smallest_gap = gap
                if smallest_gap.following is not None:
                    soln = max(soln, my_gap)
        return soln


def test_1():
    eventTime = 5
    startTime = [1,3]
    endTime = [2,5]
    expected = 2
    assert Solution().maxFreeTime(eventTime, startTime, endTime) == expected