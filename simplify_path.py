"""
LeetCode :: March 2022 Challenge :: Simplify Path
jramaswami
"""


from typing import *


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for t in path.split('/'):
            t0 = t.strip()
            if t0 == '':
                pass
            elif t0 == '..':
                if stack:
                    stack.pop()
            elif t0 == '.':
                pass
            else:
                stack.append(t0)

        return "/" + "/".join(stack)


def test_1():
    assert Solution().simplifyPath("/home/") == "/home"


def test_2():
    assert Solution().simplifyPath('/../') == '/'


def test_3():
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"


def test_4():
    assert Solution().simplifyPath( path = "/a/./b/../../c/") == "/c"
