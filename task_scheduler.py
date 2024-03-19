"""
LeetCode
621. Task Scheduler
March 2024 Challenge
jramaswami

REF: https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440
"""


import collections
from typing import List


QItem = collections.namedtuple('QItem', ['neg_ready', 'neg_freq', 'task'])


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        queue = [QItem(0, -f, t) for t, f in freqs.items()]
        max_freq = max(freqs.values())
        count_of_max_freq = sum(1 for k in freqs if freqs[k] == max_freq)
        return max((n+1) * (max_freq - 1) + count_of_max_freq, len(tasks))


def test_1():
    tasks = ["A","A","A","B","B","B"]
    n = 2
    expected = 8
    assert Solution().leastInterval(tasks, n) == expected


def test_2():
    tasks = ["A","C","A","B","D","B"]
    n = 1
    expected = 6
    assert Solution().leastInterval(tasks, n) == expected


def test_3():
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    expected = 10
    assert Solution().leastInterval(tasks, n) == expected


def test_4():
    "WA"
    tasks = ["A","B","A"]
    n = 2
    expected = 4
    assert Solution().leastInterval(tasks, n) == expected


def test_5():
    "WA"
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 1
    expected = 12
    assert Solution().leastInterval(tasks, n) == expected


def test_6():
    "WA"
    tasks = ["A","B","C","D","E","A","B","C","D","E"]
    n = 4
    expected = 10
    assert Solution().leastInterval(tasks, n) == expected