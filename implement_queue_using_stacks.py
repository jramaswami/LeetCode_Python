"""
LeetCode :: 232. Implement Queue using Stacks
jramaswami
"""
from typing import *

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out

def test_1():
    myQueue = MyQueue()
    myQueue.push(1)    # queue is: [1]
    myQueue.push(2)    # queue is: [1, 2] (leftmost is front of the queue)
    assert myQueue.peek() == 1    # return 1
    assert myQueue.pop() == 1    # return 1, queue is [2]
    assert myQueue.empty() == False    # return false
