"""
LeetCode :: February 2022 Challenge :: 402. Remove K Digits
jramaswami
"""


import collections


class Solution:

    def removeKdigits(self, num, k):
        digits = [int(d) for d in num]
        stack = collections.deque([digits[0]])
        for d in digits[1:]:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        while len(stack) > 1 and stack[0] == 0:
            stack.popleft()

        while stack and k:
            stack.pop()
            k -= 1

        return "".join(str(d) for d in stack) if stack else "0"


def test_1():
    num = "1432219"
    k = 3
    expected = "1219"
    assert Solution().removeKdigits(num, k) == expected


def test_2():
    num = "10200"
    k = 1
    expected = "200"
    assert Solution().removeKdigits(num, k) == expected


def test_3():
    num = "10"
    k = 2
    expected = "0"
    assert Solution().removeKdigits(num, k) == expected


def test_4():
    num = "8888"
    k = 2
    expected = "88"
    assert Solution().removeKdigits(num, k) == expected


def test_5():
    num = "893465"
    k = 5
    expected = "3"
    assert Solution().removeKdigits(num, k) == expected
