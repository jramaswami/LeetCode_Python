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
Task = collections.namedtuple('Task', ['key', 'priority', 'task_id', 'user_id', ])


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.current_task = dict()
        self.task_user_id = dict()
        for task in tasks:
            self.add(*task)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        key = (-priority, -task_id)
        task = Task(key, priority, task_id, user_id)
        self.task_user_id[task_id] = user_id
        self.current_task[task_id] = task
        heapq.heappush(self.heap, task)

    def edit(self, task_id: int, new_priority: int) -> None:
        user_id = self.task_user_id[task_id]
        self.add(user_id, task_id, new_priority)

    def rmv(self, task_id: int) -> None:
        self.current_task[task_id] = None

    def execTop(self) -> int:
        if not self.heap:
            return -1

        top = heapq.heappop(self.heap)
        if self.current_task[top.task_id] and top == self.current_task[top.task_id]:
            self.current_task[top.task_id] = None
            return top.user_id

        return self.execTop()


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
        print(f, p)
        r = getattr(tm, f)(*p)
        assert r == e


def test_3():
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