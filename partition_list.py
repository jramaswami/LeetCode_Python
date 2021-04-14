"""
LeetCode :: Partition List
jramaswami
"""
from leetcode_linked_lists import *


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = less_tail = None
        more_head = more_tail = None

        curr_node = head
        while curr_node:
            if curr_node.val < x:
                if not less_head:
                    less_head = curr_node
                if less_tail:
                    less_tail.next = curr_node
                less_tail = curr_node
            else:
                if not more_head:
                    more_head = curr_node
                if more_tail:
                    more_tail.next = curr_node
                more_tail = curr_node
            curr_node = curr_node.next

        if more_tail:
            more_tail.next = None
        if less_head:
            less_tail.next = more_head
            return less_head
        else:
            return more_head
                    

def test_1():
    head = [1,4,3,2,5,2]
    x = 3
    expected = [1,2,2,4,3,5]
    result = Solution().partition(make_list(head), x)
    assert make_arr(result) == expected


def test_2():
    head = [2, 1]
    x = 2
    expected = [1,2]
    result = Solution().partition(make_list(head), x)
    assert make_arr(result) == expected


def test_3():
    head = [5, 4, 3, 2]
    x = 1
    expected = list(head)
    result = Solution().partition(make_list(head), x)
    assert make_arr(result) == expected
