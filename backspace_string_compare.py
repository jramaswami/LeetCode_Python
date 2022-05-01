"""
LeetCode :: May 2022 Challenge :: 844. Backspace String Compare
jramaswami
"""


class Solution:

    def backspaceCompare(self, S, T):
        def process(X):
            stack = []
            for c in X:
                if c == '#' and stack:
                    stack.pop()
                else:
                    stack.append(c)
            return stack

        return process(S) == process(T)


def test_1():
    s = "ab#c"
    t = "ad#c"
    expected = True
    assert Solution().backspaceCompare(s, t) == expected


def test_2():
    s = "ab##"
    t = "c#d#"
    expected = True
    assert Solution().backspaceCompare(s, t) == expected


def test_3():
    s = "a#c"
    t = "b"
    expected = False
    assert Solution().backspaceCompare(s, t) == expected


def test_4():
    "WA"
    s = "y#fo##f"
    t = "y#f#o##f"
    expected = True
    assert Solution().backspaceCompare(s, t) == expected
