"""
LeetCode
1834. Single-Threaded CPU
jramaswami
"""


import heapq
import collections
from typing import *


Task = collections.namedtuple('Task', ['processing_time', 'index'])
WaitingTask = collections.namedtuple('WaitingTask', ['enqueue_time', 'task'])


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        waiting_tasks = [WaitingTask(e, Task(p, i)) for i, (e, p) in enumerate(tasks)]
        task_queue = []
        heapq.heapify(waiting_tasks)
        timer = 0
        soln = []
        while waiting_tasks or task_queue:
            # If the task queue is empty, move time forward to first enqueue
            # time.
            if not task_queue:
                timer = max(timer, waiting_tasks[0].enqueue_time)
            # Enqueue all waiting tasks that have enqueue_time <= current time.
            while waiting_tasks and waiting_tasks[0].enqueue_time <= timer:
                wt = heapq.heappop(waiting_tasks)
                heapq.heappush(task_queue, wt.task)
            # Choose the first task.
            t = heapq.heappop(task_queue)
            soln.append(t.index)
            timer += t.processing_time
        return soln


def test_1():
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    expected = [0,2,3,1]
    assert Solution().getOrder(tasks) == expected


def test_2():
    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    expected = [4,3,2,0,1]
    assert Solution().getOrder(tasks) == expected
