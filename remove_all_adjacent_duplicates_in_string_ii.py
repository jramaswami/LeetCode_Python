"""
LeetCode :: April 2021 Challenge :: Remove All Adjacent Duplicates in String II
jramaswami
"""
from collections import namedtuple


Dupe = namedtuple('Dupe', ['char', 'count'])


class Solution:
    def removeDuplicates(self, S: str, k: int) -> str:
        stack = []
        for c in S:
            if stack and stack[-1].char == c:
                stack[-1] = Dupe(c, (stack[-1].count + 1) % k)
                if stack[-1].count == 0:
                    stack.pop()
            else:
                stack.append(Dupe(c, 1))

        return "".join(c * t for c, t in stack)



def test_1():
    s = "abcd"
    k = 2
    assert Solution().removeDuplicates(s, k) == "abcd"


def test_2():
    s = "deeedbbcccbdaa"
    k = 3
    assert Solution().removeDuplicates(s, k) == "aa"


def test_3():
    s = "pbbcggttciiippooaais"
    k = 2
    assert Solution().removeDuplicates(s, k) == "ps"
