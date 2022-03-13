"""
LeetCode :: March 2022 Challenge :: Valid Parentheses
jramaswami
"""


class Solution:

    def isValid(self, S):
        stack = []
        for c in S:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
        return not stack


def test_1():
    s = "()"
    expected = True
    assert Solution().isValid(s) == expected


def test_2():
    s = "()[]{}"
    expected = True
    assert Solution().isValid(s) == expected


def test_4():
    s = "(]"
    expected = False
    assert Solution().isValid(s) == expected


def test_5():
    s = ""
    expected = True
    assert Solution().isValid(s) == expected


def test_6():
    s = "(()({[]()})"
    expected = False
    assert Solution().isValid(s) == expected
