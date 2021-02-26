"""
LeetCode :: Validate Stack Sequences
jramaswami
"""
from typing import *
from collections import deque


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_p = len(pushed) - 1
        stack = []
        for p in popped:
            stack.append(p)
            while stack and push_p >= 0 and stack[-1] == pushed[push_p]:
                stack.pop()
                push_p -= 1

        return not stack and push_p == -1


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
