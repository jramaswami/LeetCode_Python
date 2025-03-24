"""
LeetCode
3169. Count Days Without Meetings
March 2025 Challenge
jramaswami
"""


import dataclasses


@dataclasses.dataclass
class Meeting:
    start: int
    end :int

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end
        return self.start < other.start


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = [Meeting(a, b) for a, b in meetings]
        meetings.sort()
        meetings0 = []
        for m in meetings:
            if not meetings0:
                meetings0.append(m)
            elif m.start > meetings0[-1].end:
                meetings0.append(m)
            else:
                meetings0[-1].end =  max(meetings0[-1].end, m.end)
        d = sum(m.end - m.start + 1 for m in meetings0)
        return days - d