"""
LeetCode :: March 2021 Challenge :: Intersection of Two Linked Lists
jramaswami
"""
from typing import *
from leetcode_linked_lists import *


def list_len(head):
    """Return length of list."""
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    return length


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Get list lengths
        lenA = list_len(headA)
        lenB = list_len(headB)

        # Swap so that headA is the longer list.
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        nodeA = headA
        nodeB = headB

        # Advance A until it is even with B.
        for _ in range(lenA - lenB):
            nodeA = nodeA.next

        # Now move together until the lists meet.
        while nodeA:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next

        # They do not meet.
        return None



def test_1():
    intersectVal = 8
    listA = [4,1,8,4,5]
    listB = [5,6,1,8,4,5]
    skipA = 2
    skipB = 3
    
    nodesA = [ListNode(a) for a in listA]
    nodesB = [ListNode(b) for b in listB]
    nodesB[2] = nodesA[2]

    for curr, nxt in zip(nodesA[:-1], nodesA[1:]):
        curr.next = nxt

    for curr, nxt in zip(nodesB[:-1], nodesB[1:]):
        curr.next = nxt

    assert Solution().getIntersectionNode(nodesA[0], nodesB[0]) == nodesA[2]


def test_2():
    intersectVal = 2
    listA = [1,9,1,2,4]
    listB = [3,2,4]
    skipA = 3
    skipB = 1

    nodesA = [ListNode(a) for a in listA]
    nodesB = [ListNode(b) for b in listB]
    nodesB[1] = nodesA[3]

    for curr, nxt in zip(nodesA[:-1], nodesA[1:]):
        curr.next = nxt

    for curr, nxt in zip(nodesB[:-1], nodesB[1:]):
        curr.next = nxt

    assert Solution().getIntersectionNode(nodesA[0], nodesB[0]) == nodesA[3]


def test_3():
    intersectVal = 0
    listA = [2,6,4]
    listB = [1,5]
    skipA = 3
    skipB = 2

    nodesA = [ListNode(a) for a in listA]
    nodesB = [ListNode(b) for b in listB]

    for curr, nxt in zip(nodesA[:-1], nodesA[1:]):
        curr.next = nxt

    for curr, nxt in zip(nodesB[:-1], nodesB[1:]):
        curr.next = nxt

    assert Solution().getIntersectionNode(nodesA[0], nodesB[0]) == None
