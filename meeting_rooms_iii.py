"""
LeetCode
2402. Meeting Rooms III
February 2023 Challenge
jramaswami
"""


import collections
import heapq
from typing import *


Room = collections.namedtuple('Room', ['time', 'id'])
Meeting = collections.namedtuple('Meeting', ['start', 'end'])


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomq = [Room(0, x) for x in range(n)]
        heapq.heapify(roomq)
        meetingq = collections.deque(sorted(Meeting(s, e) for s, e in meetings))

        room_meetings = [0 for _ in range(n)]
        while meetingq:
            meeting = meetingq.popleft()
            room = heapq.heappop(roomq)
            room_meetings[room.id] += 1
            meeting_time = meeting.end - meeting.start
            print(meeting, room, '->', meeting_time, '+', Room(max(room.time, meeting.start) + meeting_time, room.id))
            heapq.heappush(roomq, Room(max(room.time, meeting.start) + meeting_time, room.id))

        print(room_meetings)
        soln_room = 0
        soln_meetings = 0
        for room_id, meeting_count in enumerate(room_meetings):
            if meeting_count > soln_meetings:
                soln_room, soln_meetings = room_id, meeting_count
        return soln_room


def test_1():
    n = 2
    meetings = [[0,10],[1,5],[2,7],[3,4]]
    expected = 0
    assert Solution().mostBooked(n, meetings) == expected


def test_2():
    n = 3
    meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    expected = 1
    assert Solution().mostBooked(n, meetings) == expected


def test_3():
    "WA"
    n = 4
    meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
    expected = 0
    assert Solution().mostBooked(n, meetings) == expected