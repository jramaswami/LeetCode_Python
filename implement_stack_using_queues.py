"""
LeetCode :: May 2022 Challenge :: 225. Implement Stack using Queues
jramaswami
"""


import collections


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        k = len(self.queue)
        for _ in range (k-1):
            self.queue.append(self.queue.popleft())
        x = self.queue.popleft()
        return x

    def top(self) -> int:
        k = len(self.queue)
        for _ in range (k-1):
            self.queue.append(self.queue.popleft())
        x = self.queue[0]
        self.queue.append(self.queue.popleft())
        return x

    def empty(self) -> bool:
        return len(self.queue) == 0
