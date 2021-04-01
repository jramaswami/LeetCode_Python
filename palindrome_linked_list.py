"""
LeetCode :: April 2021 Challenge :: Palindrome Linked List
jramaswami
"""
from typing import *
from leetcode_linked_lists import *


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Get the length of the list and the tail.
        length = 0
        node = head
        tail = None
        while node:
            length += 1
            tail = node
            node = node.next

        if length == 1:
            return True
        
        # Find the center node of the list.
        mid = (length // 2)
        center_prev = None
        center = head
        for _ in range(mid):
            center_prev = center
            center = center.next

        # If the length is odd, we can ignore the middle element
        if length % 2:
            right_head = center.next
        else:
            right_head = center
        # Break lists
        center_prev.next = None

        # Reverse the links from the center node to the tail.
        prev = None
        curr = right_head
        follow = right_head
        while curr:
            follow = follow.next
            curr.next = prev
            prev = curr
            curr = follow

        # See if the two lists are the same
        left_curr = head
        right_curr = tail
        soln = True
        while left_curr and right_curr:
            if left_curr.val != right_curr.val:
                soln = False
                break
            left_curr = left_curr.next
            right_curr = right_curr.next

        # Reverse the links from the tail to the center node.
        prev = None
        curr = tail
        follow = tail
        while curr:
            follow = follow.next
            curr.next = prev
            prev = curr
            curr = follow

        # Connect everything again
        if length % 2:
            center.next = right_head
        center_prev.next = center

        return soln


def test_1():
    head = make_list([1, 2, 2, 1])
    assert Solution().isPalindrome(head) == True


def test_2():
    head = make_list([1, 2])
    assert Solution().isPalindrome(head) == False


def test_3():
    head = make_list([1, 2, 7, 2, 1])
    assert Solution().isPalindrome(head) == True


def test_4():
    head = make_list([1, 2, 3, 4, 5])
    assert Solution().isPalindrome(head) == False

