"""
LeetCode :: 1235. Maximum Profit in Job Scheduling
November 2022 Challenge
jramaswami

Thank You Larry!
"""


from typing import *
import collections
import heapq


Job = collections.namedtuple('Job', ['start', 'type', 'end', 'profit'])
START = 1
END = 0


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = [Job(s, START, e, p) for s, e, p in zip(startTime, endTime, profit)]
        heapq.heapify(events)
        curr_best_profit = 0
        while events:
            j = heapq.heappop(events)
            if j.type == START:
                heapq.heappush(events, Job(j.end, END, -1, curr_best_profit + j.profit))
            else:
                curr_best_profit = max(curr_best_profit, j.profit)
        return curr_best_profit


def test_1():
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    expected = 120
    assert Solution().jobScheduling(startTime, endTime, profit) == expected


def test_2():
    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    expected = 150
    assert Solution().jobScheduling(startTime, endTime, profit) == expected


def test_3():
    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]
    expected = 6
    assert Solution().jobScheduling(startTime, endTime, profit) == expected