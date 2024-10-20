"""
LeetCode
1106. Parsing A Boolean Expression
October 2024 Challenge
jramaswami
"""


import functools
import operator


def tokenize(expr):
    in_subexpr = False
    tokens = []
    curr_token = []
    curr_parens = 0
    for c in expr[2:-1]:
        if in_subexpr:
            curr_token.append(c)
            if c == ')':
                curr_parens -= 1
                if curr_parens == 0:
                    in_subexpr = False
            elif c == '(':
                curr_parens += 1
        else:
            if c in ('!&|'):
                curr_token.append(c)
                in_subexpr = True
                curr_parens = 0
            elif c == ',':
                tokens.append(''.join(curr_token))
                curr_token = []
            else:
                curr_token.append(c)
    if curr_token:
        tokens.append(''.join(curr_token))
    return tokens


def parse(expr):
    if expr.startswith('!'):
        # logical not
        return operator.not_(parse(expr[2:-1]))
    elif expr.startswith('&'):
        # logical and
        subexprs = [parse(t) for t in tokenize(expr)]
        if len(subexprs) == 1:
            return subexprs[0]
        return functools.reduce(operator.and_, subexprs)
    elif expr.startswith('|'):
        # logical or
        subexprs = [parse(t) for t in tokenize(expr)]
        if len(subexprs) == 1:
            return subexprs[0]
        return functools.reduce(operator.or_, subexprs)
    elif expr == 't':
        return True
    elif expr == 'f':
        return False
    else:
        print(f'Nope! {expr=}')
        assert False


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:\
        return parse(expression)


def test_1():
    expression = "&(|(f))"
    expected = False
    return Solution().parseBoolExpr(expression) == expected


def test_2():
    expression = "|(f,f,f,t)"
    expected = True
    return Solution().parseBoolExpr(expression) == expected


def test_3():
    expression = "!(&(f,t))"
    expected = True
    return Solution().parseBoolExpr(expression) == expected


def test_4():
    expression = "|(&(t,f,t),!(t))"
    expected = False
    return Solution().parseBoolExpr(expression) == expected