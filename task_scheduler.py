"""
LeetCode
621. Task Scheduler
March 2024 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        ready = {k: 0 for k in freqs}
        queue = collections.deque(sorted(((v, k) for k, v in freqs.items()), reverse=True))
        timer = 0
        while queue:
            count, task = queue.popleft()
            print(count, task, ready[task], timer)
            timer = max(timer, ready[task])
            if count - 1 > 0:
                queue.append((count - 1, task))
                ready[task] = timer + n + 1
            timer += 1
        return timer


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