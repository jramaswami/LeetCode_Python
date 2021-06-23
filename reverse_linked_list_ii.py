"""
LeetCode :: June 2021 Challenge :: Reverse Linked List II
jramaswami
"""


from collections import deque


class Solution:
    def reverseBetween(self, head, left, right):

        def solve(node, index, acc):
            if node is None:
                return

            if left <= index <= right:
                acc.append(node.val)

            solve(node.next, index + 1, acc)

            if left <= index <= right:
                node.val = acc.popleft()

        solve(head, 1, deque())
        return head


#
# Testing
#
from leetcode_linked_lists import *


def test_1():
    head = [1,2,3,4,5]
    left = 2
    right = 4
    expected = [1,4,3,2,5]
    assert make_arr(Solution().reverseBetween(make_list(head), left, right)) == expected


def test_2():
    head = [5]
    left = 1
    right = 1
    expected = [5]
    assert make_arr(Solution().reverseBetween(make_list(head), left, right)) == expected
