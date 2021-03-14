"""
LeetCode :: March 2021 Challenge :: Swapping Nodes in a Linked List
jramaswami
"""
from typing import *
from leetcode_linked_lists import *


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Find the kth element, its predecessor, and the length
        previous_left = None
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
        previous_right = None
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

        # If nodes have crossed, switch left and right.
        if k0 < k:
            current_left, current_right = current_right, current_left
            previous_left, previous_right = previous_right, previous_left

        # Swap the nodes
        following_left = current_left.next
        following_right = current_right.next
        if current_left == current_right:
            # There is nothing to do if they are the same node.
            pass
        elif current_right == current_left.next:
            # Swapping adjacent nodes is different
            if previous_left:
                previous_left.next = current_right
            current_right.next = current_left
            current_left.next = following_right
        else:
            if previous_left:
                previous_left.next = current_right
            current_right.next = following_left
            if previous_right:
                previous_right.next = current_left
            current_left.next = following_right

        # If you swapped the head, change it.
        if current_left == head:
            head = current_right

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
