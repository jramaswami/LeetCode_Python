"""
LeetCode :: May 2022 Challenge :: Intersection of Two Linked Lists
jramaswami
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Important observations:
        # Linked list must retain their structures *after* function returns.
        # 1 <= Node.val <= 105

        def flipSign(head):
            curr = head
            while curr:
                curr.val *= -1
                curr = curr.next

        flipSign(headA)
        soln = headB
        while soln and soln.val > 0:
            soln = soln.next
        flipSign(headA)
        return soln


#
# TESTING
#


from leetcode_linked_lists import *


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
