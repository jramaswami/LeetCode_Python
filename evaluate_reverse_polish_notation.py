"""
LeetCode :: May 2021 Challenge :: Evaluate Reverse Polish Notation
jramaswami
"""


from typing import *
from operator import add, sub, mul
from math import ceil


def toward_zero_div(a, b):
    """Return a / b truncated toward zero."""
    c = a / b
    if c >= 0:
        return int(c)
    else:
        return int(ceil(c))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+": add, "-": sub, "*": mul, "/": toward_zero_div}
        stack = []
        for t in tokens:
            if t in operators.keys():
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a, b))
            else:
                stack.append(int(t))
        return stack[-1]



def test_1():
    tokens = ["2","1","+","3","*"]
    assert Solution().evalRPN(tokens) == 9


def test_2():
    tokens = ["4","13","5","/","+"]
    assert Solution().evalRPN(tokens) == 6


def test_1():
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert Solution().evalRPN(tokens) == 22