"""
LeetCode
731. My Calendar II
September 2024 Challenge
jramaswami
"""


START, END = 0, 1


class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        events0 = list(self.events)
        events0.append((start, end-0.01))
        events0.sort()
        
        curr_events = []
        for evt in events0:
            curr_events = [x for x in curr_events if x[END] >= evt[START]]
            curr_events.append(evt)
            if len(curr_events) > 2:
                return False
        self.events = events0
        return True
