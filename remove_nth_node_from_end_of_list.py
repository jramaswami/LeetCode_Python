"""
LeetCode :: September 2022 Challenge :: 19. Remove Nth Node From End of List
jramaswami
"""


from typing import *
from leetcode_linked_lists import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            nodes[-1].next = None
        nodes[-n] = None
        dummy = ListNode(0)
        curr = dummy
        for node in nodes:
            if node is not None:
                curr.next = node
                curr = node
        return dummy.next


def test_1():
    head = [1,2,3,4,5]
    n = 2
    expected = [1,2,3,5]
    result = Solution().removeNthFromEnd(make_list(head), n)
    print(result)
    assert make_arr(result) == expected


def test_2():
    head = [1]
    n = 1
    result = Solution().removeNthFromEnd(make_list(head), n)
    expected = []
    print(result)
    assert make_arr(result) == expected


def test_3():
    head = [1,2]
    n = 1
    expected = [1]
    result = Solution().removeNthFromEnd(make_list(head), n)
    print(result)
    assert make_arr(result) == expected