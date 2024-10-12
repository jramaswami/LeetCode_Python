"""
LeetCode
2406. Divide Intervals Into Minimum Number of Groups
October 2024 Challenge
jramaswami
"""


import collections


Event = collections.namedtuple('Event', ['time', 'type'])


START = 0
END = 1


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start_t, end_t in intervals:
            events.append(Event(start_t, START))
            events.append(Event(end_t, END))
        events.sort()

        soln = 0
        curr_count = 0
        for event in events:
            if event.type == START:
                curr_count += 1
            else:
                curr_count -= 1
            soln = max(soln, curr_count)
        return soln
