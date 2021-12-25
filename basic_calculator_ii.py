"""
LeetCode :: December 2021 Challenge :: 227. Basic Calculator II
jramaswami
"""


import collections
import operator


class Solution:

    def calculate(self, expr):
        tokens = collections.deque()
        parsing_number = False
        number = 0
        for c in expr:
            if c.isdigit():
                number *= 10
                number += int(c)
                parsing_number = True
            else:
                if parsing_number:
                    tokens.append(number)
                    number  = 0
                    parsing_number = False
                if c in '+-*/':
                    tokens.append(c)
        if parsing_number:
            tokens.append(number)

        ops = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': lambda a, b: int(a / b)
        }

        eval0 = collections.deque()
        while tokens:
            token = tokens.popleft()
            if token in ("*", "/"):
                lhs = eval0.pop()
                rhs = tokens.popleft()
                result = ops[token](lhs, rhs)
                eval0.append(result)
            else:
                eval0.append(token)

        lhs = eval0.popleft()
        while eval0:
            op = eval0.popleft()
            rhs = eval0.popleft()
            lhs = ops[op](lhs, rhs)
        return lhs


def test_1():
    expr = "3+2*2"
    assert Solution().calculate(expr) == 7


def test_2():
    expr = " 3/2 "
    assert Solution().calculate(expr) == 1


def test_3():
    expr = " 3+5 / 2 "
    assert Solution().calculate(expr) == 5
