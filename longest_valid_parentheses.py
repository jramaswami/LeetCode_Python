"""
LeetCode :: Longest Valid Parentheses
jramaswami
"""
from typing import *


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        soln = 0
        last_good_start = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        soln = max(soln, i - stack[-1])
                    else:
                        soln = max(soln, i - last_good_start)
                else:
                    last_good_start = i
        return soln


def test_1():
    assert Solution().longestValidParentheses("(()") == 2

def test_2():
    assert Solution().longestValidParentheses(")()())") == 4

def test_3():
    assert Solution().longestValidParentheses("") == 0

def test_4():
    assert Solution().longestValidParentheses("(((()()((()((()()()()(((()()()()()()()()()()((((()()()(()()()()()()") == 20

def test_5():
    """WA"""
    assert Solution().longestValidParentheses("()") == 2
