"""
LeetCode :: Minimum Remove to Make Valid Parentheses
jramaswami
"""
from typing import *


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parentheses = [(c, i) for i, c in enumerate(s) if c == ')' or c == '(']
        
        # Left to right
        stack = []
        removed_left = []
        for c, i in parentheses:
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    removed_left.append(i)
        while stack:
            c, i = stack.pop()
            removed_left.append(i)

        # Right to left
        stack = []
        removed_right = []
        for c, i in reversed(parentheses):
            if c == ')':
                stack.append((c, i))
            elif c == '(':
                if stack:
                    stack.pop()
                else:
                    removed_right.append(i)
        while stack:
            c, i = stack.pop()
            removed_right.append(i)

        # Form longest string
        s0 = list(s)
        for i in min(removed_left, removed_right, key=len):
            s0[i] = ""
        return "".join(s0)


def test_1():
    s = "lee(t(c)o)de)"
    expected = "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid(s) == expected

def test_2():
    s = "a)b(c)d"
    expected = "ab(c)d"
    assert Solution().minRemoveToMakeValid(s) == expected

def test_3():
    s = "))(("
    expected = ""
    assert Solution().minRemoveToMakeValid(s) == expected

def test_4():
    s = "(a(b(c)d)"
    expected = "a(b(c)d)"
    assert Solution().minRemoveToMakeValid(s) == expected

def test_5():
    s = "a(b(c)(d)e)f"
    expected = "a(b(c)(d)e)f"
    assert Solution().minRemoveToMakeValid(s) == expected

