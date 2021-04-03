"""
LeetCode :: Longest Valid Parentheses
jramaswami
"""
from typing import *


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack with -1 marker as beginning.
        stack = [-1]
        # Initial solution.
        soln = 0
        # Iterate over string.
        for i, c in enumerate(s):
            if c == '(':
                # If this is an opening, push the index on the stack.
                stack.append(i)
            else:
                # If this is a closing, pop the opening off the stack.
                stack.pop()
                if stack:
                    # If the stack is not empty, then we are valid up to
                    # any unbalanced close or to the beginning. See if it
                    # is the maximum length valid string.
                    soln = max(soln, i - stack[-1])
                else:
                    # If the stack is empty, then it is invalid and we
                    # have to mark that valid strings start after this
                    # close, so push its index onto the stack.
                    stack.append(i)
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
