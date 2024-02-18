"""
LeetCode
2402. Meeting Rooms III
February 2023 Challenge
jramaswami
"""


import collections
import heapq
from typing import *


Event = collections.namedtuple('Event', ['time', 'type', 'id'])
Room = collections.namedtuple('Room', ['id', 'time'])
Meeting = collections.namedtuple('Meeting', ['start', 'end'])


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        eventq = [Event(0, 'room', x) for x in range(n)]
        eventq.extend(Event(m[0], 'meeting', i) for i, m in enumerate(meetings))
        heapq.heapify(eventq)
        room_meetings = [0 for _ in range(n)]
        roomq = []
        meetingq = []

        # While there are events left or meetings
        while eventq or meetingq:
            # Take all the events that occur at the time, t, of the first
            # event in the event queue
            while eventq and ((not roomq) or (not meetingq)):
                t = eventq[0].time
                while eventq and eventq[0].time == t:
                    event = heapq.heappop(eventq)
                    if event.type == 'room':
                        heapq.heappush(roomq, Room(event.id, event.time))
                    else:
                        heapq.heappush(meetingq, Meeting._make(meetings[event.id]))

            # For every pair of rooms and meetings that are available,
            # start the meeting in the given room
            while roomq and meetingq:
                room = heapq.heappop(roomq)
                meeting = heapq.heappop(meetingq)
                room_meetings[room.id] += 1
                meeting_time = meeting.end - meeting.start
                actual_meeting_start = max(meeting.start, room.time)
                actual_meeting_end = actual_meeting_start + meeting_time
                heapq.heappush(eventq, Event(actual_meeting_end, 'room', room.id))

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