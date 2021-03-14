"""
LeetCode :: March 2021 Challenge :: Swapping Nodes in a Linked List
jramaswami
"""
from typing import *
from leetcode_linked_lists import *


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Find the kth element, its predecessor, and the length
        current_left =  None
        left_index = 0
        length = 0

        node = head
        while node:
            if left_index < k:
                left_index += 1
                previous_left = current_left
                current_left = node
            node = node.next
            length += 1

        # Find the -kth node and its predecessor
        k0 = length - k + 1
        current_right =  None
        right_index = 0
        length = 0

        node = head
        while node:
            if right_index < k0:
                right_index += 1
                previous_right = current_right
                current_right = node
            node = node.next

        # Swap values
        current_left.val, current_right.val = current_right.val, current_left.val

        return head


def test_1():
     head = make_list([1,2,3,4,5])
     k = 2
     assert make_arr(Solution().swapNodes(head, k)) == [1,4,3,2,5]

def test_2():
    head = make_list([1])
    k = 1
    assert make_arr(Solution().swapNodes(head, k)) == [1]

def test_3():
    head = make_list([1,2])
    k = 1
    assert make_arr(Solution().swapNodes(head, k)) == [2, 1]

def test_4():
    head = make_list([1,2,3])
    k = 2
    assert make_arr(Solution().swapNodes(head, k)) == [1, 2, 3]

def test_5():
    head = make_list([100,90])
    k = 2
    assert make_arr(Solution().swapNodes(head, k)) == [90, 100]
