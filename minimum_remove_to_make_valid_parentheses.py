"""
LeetCode :: March 2022 Challenge :: Minimum Remove to Make Valid Parentheses
jramaswami
"""


class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        l2r = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    l2r.append(i)
        l2r.extend(stack)

        stack = []
        r2l = []
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == ')':
                stack.append(i)
            elif c == '(':
                if stack:
                    stack.pop()
                else:
                    r2l.append(i)
        r2l.extend(stack)

        removals = l2r
        if len(r2l) < len(l2r):
           removals = r2l

        letters = list(s)
        for i in removals:
            letters[i] = ""
        return "".join(letters)


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
