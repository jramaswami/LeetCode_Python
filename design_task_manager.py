"""
LeetCode
3408. Design Task Manager
September 2025 Challenge
jramaswami
"""


import collections
import heapq
from typing import List


REMOVED = 0
Task = collections.namedtuple('Task', ['priority', 'user_id', 'task_id'])


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.current_priority = dict()
        self.task_user_id = dict()
        for task in tasks:
            self.add(*task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(-priority, -userId, taskId)
        self.task_user_id[taskId] = userId
        self.current_priority[taskId] = -priority
        heapq.heappush(self.heap, task)

    def edit(self, taskId: int, newPriority: int) -> None:
        self.current_priority[taskId] = -newPriority
        task = Task(-newPriority, -self.task_user_id[taskId], taskId)
        heapq.heappush(self.heap, task)

    def rmv(self, taskId: int) -> None:
        self.current_priority[taskId] = REMOVED

    def execTop(self) -> int:
        if not self.heap:
            return -1

        top = heapq.heappop(self.heap)
        while 1:
            if top.priority == self.current_priority[top.task_id]:
                break
            if not self.heap:
                return -1
            top = heapq.heappop(self.heap)

        self.current_priority[top.task_id] = REMOVED
        return -top.user_id


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


null = None


def test_1():
    fns = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
    params = [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]
    es = [null, null, null, 3, null, null, 5]
    tm = TaskManager(*params[0])
    for f, p, e in zip(fns[1:], params[1:], es[1:]):
        r = getattr(tm, f)(*p)
        assert r == e


def test_2():
    "WA"
    fns = ["TaskManager","add","edit","execTop","rmv","add","execTop"]
    params = [[[[1,101,8],[2,102,20],[3,103,5]]],[4,104,5],[102,9],[],[101],[50,101,8],[]]
    es = [null,null,null,2,null,null,50]
    tm = TaskManager(*params[0])
    for f, p, e in zip(fns[1:], params[1:], es[1:]):
        r = getattr(tm, f)(*p)
        assert r == e


def test_2():
    "WA"
    fns = ["TaskManager","execTop"]
    params = [[[[10,4,10],[10,0,6],[5,23,50],[3,29,50],[2,15,9]]],[]]
    es = [null,3]
    tm = TaskManager(*params[0])
    for f, p, e in zip(fns[1:], params[1:], es[1:]):
        r = getattr(tm, f)(*p)
        assert r == e


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()