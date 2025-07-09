"""
LeetCode
3439. Reschedule Meetings for Maximum Free Time I
July 2025 Challenge
jramaswami
"""


import collections
from typing import List



Meeting = collections.namedtuple('Meeting', ['start', 'end', 'duration'])


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        meetings = [Meeting(s, e, e-s) for s, e in zip(startTime, endTime)]
        meetings.append(Meeting(eventTime, eventTime, 0))
        window = collections.deque()
        window.append(Meeting(0, 0, 0))
        soln = 0
        meetings_duration = 0
        # What is the most free time right now?
        for meeting in meetings:
            while len(window) > k + 1:
                window.popleft()
                meetings_duration -= window[0].duration
            # Create window with
            # non-moving-meeting[0], moving meetings ..., non-moving meeting[-1]
            # Compute or store the duration of moving meetings, Y
            # Compute duration from window[0].end to window[-1].start, X
            # The shifting the moving meetings will allow you to have X - Y free time
            meetings_duration += window[-1].duration
            window.append(meeting)
            if len(window) > 2:
                window_duration = window[-1].start - window[0].end
                soln = max(soln, window_duration - meetings_duration)
        return soln


def test_1():
    eventTime = 5
    k = 1
    startTime = [1,3]
    endTime = [2,5]
    expected = 2
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == expected


def test_2():
    eventTime = 10
    k = 1
    startTime = [0,2,9]
    endTime = [1,4,10]
    expected = 6
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == expected


def test_3():
    eventTime = 5
    k = 2
    startTime = [0,1,2,3,4]
    endTime = [1,2,3,4,5]
    expected = 0
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == expected


def test_4():
    "WA"
    eventTime = 21
    k = 1
    startTime = [7,10,16]
    endTime = [10,14,18]
    expected = 7
    assert Solution().maxFreeTime(eventTime, k, startTime, endTime) == expected