"""
LeetCode :: Validate Stack Sequences
jramaswami
"""
from typing import *
from collections import deque


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_p = 0
        stack = []
        for p in pushed:
            stack.append(p)
            while stack and pop_p < len(popped) and stack[-1] == popped[pop_p]:
                stack.pop()
                pop_p += 1

        return not stack and pop_p == len(popped)


def test_1():
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    assert Solution().validateStackSequences(pushed, popped) == True

def test_2():
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    assert Solution().validateStackSequences(pushed, popped) == False

def test_3():
    pushed = [1,0,2]
    popped = [2,1,0]
    assert Solution().validateStackSequences(pushed, popped) == False
