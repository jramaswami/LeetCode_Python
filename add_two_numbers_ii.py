"""
LeetCode
445. Add Two Numbers II
July 2023 Challenge
jramaswami
"""


from collections import deque
from itertools import zip_longest
from typing import Optional
from leetcode_linked_lists import ListNode, make_arr, make_list


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = deque()
        t = l1
        while t:
            x.appendleft(t.val)
            t = t.next

        y = deque()
        t = l2
        while t:
            y.appendleft(t.val)
            t = t.next

        z = []
        c = 0
        for a, b in zip_longest(x, y, fillvalue=0):
            t = a + b + c
            c = 0
            if t >= 10:
                t, c = t % 10, 1
            z.append(t)
        if c:
            z.append(c)

        dummy = ListNode(-1)
        curr = dummy
        while z:
            curr.next = ListNode(z[-1])
            curr = curr.next
            z.pop()
        return dummy.next


def test_1():
    l1 = [7,2,4,3]
    l2 = [5,6,4]
    expected = [7,8,0,7]
    result = make_arr(Solution().addTwoNumbers(make_list(l1), make_list(l2)))
    assert result == expected


def test_2():
    l1 = [2,4,3]
    l2 = [5,6,4]
    expected = [8,0,7]
    result = make_arr(Solution().addTwoNumbers(make_list(l1), make_list(l2)))
    assert result == expected


def test_3():
    l1 = [0]
    l2 = [0]
    expected = [0]
    result = make_arr(Solution().addTwoNumbers(make_list(l1), make_list(l2)))
    assert result == expected