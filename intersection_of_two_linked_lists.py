"""
LeetCode :: March 2021 Challenge :: Intersection of Two Linked Lists
jramaswami
"""
from typing import *
from leetcode_linked_lists import *


def reverse_linked_list(node):
    """Reverse the linked list in place."""
    previous = None
    current = node
    following = node

    while current:
        following = following.next
        current.next = previous
        previous = current
        current = following

    return previous



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Reverse the lists
        headA = reverse_linked_list(headA)
        headB = reverse_linked_list(headB)

        nodeA = headA
        nodeB = headB

        soln = None
        while nodeA and nodeB and nodeA == nodeB:
            soln = nodeA
        return soln

        # Put lists back in previous order
        headA = reverse_linked_list(headA)
        headB = reverse_linked_list(headB)

