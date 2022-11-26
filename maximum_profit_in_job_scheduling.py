"""
LeetCode :: 1235. Maximum Profit in Job Scheduling
November 2022 Challenge
jramaswami
"""


from typing import *
import collections
import functools


Job = collections.namedtuple('Job', ['start', 'end', 'profit'])


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [Job(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.append(Job(-1, 0, 0))  # Dummy job to get started.
        jobs.sort()


        def find_next_jobs(prev_job):
            "Given previous job, return the starting index of possible next jobs."
            lo = prev_job + 1
            hi = len(jobs) - 1
            result = hi + 1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if jobs[mid].start >= jobs[prev_job].end:
                    result = min(result, mid)
                    hi = mid - 1
                else:
                    lo = mid + 1
            return result

        @functools.cache
        def rec(prev_job):
            "Recursive DP."
            if prev_job >= len(jobs):
                return 0

            result = 0
            start_of_next_jobs = find_next_jobs(prev_job)
            for next_job, _ in enumerate(jobs[start_of_next_jobs:], start = start_of_next_jobs):
                result = max(
                    result,
                    jobs[next_job].profit + rec(next_job)
                )
            return result

        return rec(0)



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